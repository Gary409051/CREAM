#!/usr/bin/env python3
"""Read-only scaffold checks. Not scientific, security or external-source validation."""

import ast
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md", "CONTRIBUTING.md", "LICENSE_DECISION.md", ".gitignore",
    "pyproject.toml", "docs/RESEARCH_ROADMAP.md",
    "docs/RESEARCH_QUESTIONS_AND_HYPOTHESES.md", "docs/EXPERIMENT_PROTOCOLS.md",
    "docs/LITERATURE_REVIEW.md", "docs/DECISIONS.md", "docs/DATA_MANAGEMENT.md",
    "docs/REPRODUCIBILITY.md", "docs/ETHICS.md", "papers/v1/README.md",
    "papers/v1/originals.sha256.json", "configs/README.md",
    "configs/e1_residual_validation.draft.json", "data/manifests/manifest.schema.json",
    "src/cream/__init__.py", "src/cream/data.py", "src/cream/acoustics.py",
    "src/cream/baselines.py", "src/cream/residuals.py", "src/cream/representations.py",
    "src/cream/alignment.py", "src/cream/synthesis.py", "src/cream/evaluation.py",
    "tests/README.md", "scripts/README.md", "experiments/README.md",
    "experiments/preregistrations/README.md", "experiments/reports/README.md",
)
EMPTY_DIRS = (
    "data/raw", "data/interim", "data/processed", "data/external",
    "tests/unit", "tests/integration", "tests/fixtures", "experiments/runs",
)
ORIGINALS = (
    "CREAM_Research_Paper_v1.pdf", "CREAM_Research_Paper_v1.docx",
    "LECR_Research_Manuscript_v1.md",
)


def unfenced(text):
    """Strip fenced examples before scanning headings and inline Markdown links."""
    result = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker[0]
            elif marker[0] == fence:
                fence = None
            continue
        if fence is None:
            result.append(line)
    return "\n".join(result)


def heading_anchors(path):
    anchors = set()
    duplicates = {}
    for line in unfenced(path.read_text(encoding="utf-8")).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = re.sub(r"[`*_]", "", match.group(1)).lower()
            slug = re.sub(r"[^\w\- ]", "", title).replace(" ", "-")
            count = duplicates.get(slug, 0)
            duplicates[slug] = count + 1
            anchors.add(slug if count == 0 else "{}-{}".format(slug, count))
    return anchors


def main():
    errors = []
    for relative in REQUIRED_FILES + ORIGINALS:
        if not (ROOT / relative).is_file():
            errors.append("Missing required file: " + relative)
    for relative in EMPTY_DIRS:
        if not (ROOT / relative / ".gitkeep").is_file():
            errors.append("Missing placeholder: " + relative)

    archive = ROOT / "papers/v1/originals.sha256.json"
    try:
        recorded = json.loads(archive.read_text(encoding="utf-8"))["files"]
        if set(recorded) != set(ORIGINALS):
            errors.append("Archive manifest does not name exactly the three originals")
        for relative in ORIGINALS:
            path = ROOT / relative
            if path.is_file():
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                if recorded.get(relative) != digest:
                    errors.append("Original checksum changed: " + relative)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("Archive manifest error: " + str(exc))

    markdown = sorted(
        path for path in ROOT.rglob("*.md")
        if ".git" not in path.relative_to(ROOT).parts
        and not any(part in {".venv", "venv", "local"} for part in path.relative_to(ROOT).parts)
        and path.relative_to(ROOT).as_posix() not in ORIGINALS
        and not path.relative_to(ROOT).as_posix().startswith((
            "data/raw/", "data/interim/", "data/processed/", "data/external/",
            "experiments/runs/",
        ))
    )
    local_links = 0
    for path in markdown:
        for raw in re.findall(r"!?\[[^\]]*\]\(([^\n]*?)\)", unfenced(path.read_text(encoding="utf-8"))):
            target = raw.strip()
            if target.startswith("<") and ">" in target:
                target = target[1:target.index(">")]
            else:
                target = target.split(' "', 1)[0].split(" '", 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc:
                continue
            local_links += 1
            linked = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not linked.exists():
                errors.append("{}: broken local link {}".format(path.relative_to(ROOT), target))
            elif parsed.fragment and linked.suffix == ".md":
                if unquote(parsed.fragment) not in heading_anchors(linked):
                    errors.append("{}: missing heading {}".format(path.relative_to(ROOT), target))

    config_path = ROOT / "configs/e1_residual_validation.draft.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if config["frozen"] is not False or config["status"] != "draft_not_preregistered":
            errors.append("E1 draft was mislabeled as frozen/registered")
        if config["numeric_values_are_candidates"] is not True:
            errors.append("E1 candidate values require an explicit draft marker")
        if config["neutral_is_primary_class"] or "neutral" in config["primary_labels"]:
            errors.append("E1 primary target must not use neutral self-subtraction")
        if config["test_speaker_neutral_support_allowed"] or config["target_expressive_labels_for_fitting_allowed"]:
            errors.append("E1-P calibration permissions disagree with the draft protocol")
        for key in ("speaker_proportions", "text_proportions"):
            proportions = config["split"][key]
            if len(proportions) != 3 or any(p <= 0 for p in proportions) or abs(sum(proportions) - 1) > 1e-9:
                errors.append("Invalid candidate split proportions: " + key)
        if config["inference"]["primary_family_size"] != len(config["directions"]):
            errors.append("Primary directional family size mismatch")
        if len(config["seeds"]) != len(set(config["seeds"])):
            errors.append("Duplicate seeds")
        json.loads((ROOT / "data/manifests/manifest.schema.json").read_text(encoding="utf-8"))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("JSON/config error: " + str(exc))

    python_paths = sorted((ROOT / "src/cream").glob("*.py")) + [Path(__file__).resolve()]
    for path in python_paths:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            errors.append("Python syntax error: " + str(exc))

    # Read-only Git checks on both existing placeholders and nonexistent sample paths.
    try:
        tracked = subprocess.run(
            ["git", "ls-files", "--", *ORIGINALS], cwd=ROOT,
            capture_output=True, text=True, check=True,
        ).stdout.splitlines()
        if set(tracked) != set(ORIGINALS):
            errors.append("Original paths are no longer all Git tracked")
        keep_paths = [relative + "/.gitkeep" for relative in EMPTY_DIRS]
        ignored_keep = subprocess.run(
            ["git", "check-ignore", "--no-index", "--stdin"], cwd=ROOT,
            input="\n".join(keep_paths) + "\n", capture_output=True, text=True,
        )
        if ignored_keep.returncode not in (0, 1):
            errors.append("Git ignore check failed: " + ignored_keep.stderr.strip())
        elif ignored_keep.stdout.strip():
            errors.append("Placeholders ignored by Git: " + ignored_keep.stdout.strip())
        private_paths = [
            "data/raw/example.wav", "data/interim/example.json", "data/processed/features.json",
            "data/external/model.bin", "data/manifests/example.private.jsonl",
            "experiments/runs/example/run.json", ".env",
        ]
        ignored_private = subprocess.run(
            ["git", "check-ignore", "--no-index", "--stdin"], cwd=ROOT,
            input="\n".join(private_paths) + "\n", capture_output=True, text=True,
        )
        if ignored_private.returncode not in (0, 1):
            errors.append("Git private-path check failed: " + ignored_private.stderr.strip())
        elif set(ignored_private.stdout.splitlines()) != set(private_paths):
            errors.append("Private-data/output ignore rules incomplete")
    except (OSError, subprocess.CalledProcessError) as exc:
        errors.append("Git read-only validation failed: " + str(exc))

    if errors:
        for error in errors:
            print("FAIL: " + error, file=sys.stderr)
        return 1
    print("PASS: required structure and {} placeholders".format(len(EMPTY_DIRS)))
    print("PASS: {} authored Markdown files / {} local links".format(len(markdown), local_links))
    print("PASS: all three original hashes and Git-tracked paths unchanged")
    print("PASS: draft E1 configuration, JSON and {} Python syntax checks".format(len(python_paths)))
    print("PASS: private-data/output ignore rules; placeholders remain visible")
    print("LIMIT: no remote-link, algorithm, data, statistical or empirical validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
