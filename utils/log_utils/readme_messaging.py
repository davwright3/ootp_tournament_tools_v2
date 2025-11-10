import logging
import pathlib
import re
from typing import Optional

logger = logging.getLogger(__name__)


# Use a Github-like slug to pass visible heading or anchor
def _sluggify_github(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'\s+', '-', s)
    s = re.sub(r'-{2,}', '-', s)
    return s


def extract_markdown_section(
        md_path: str,
        heading_query: str) -> Optional[str]:
    """Return the markdown content under the first
    heading matching 'heading_query'."""
    p = pathlib.Path(md_path)
    if not p.exists():
        return None

    lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
    target_slug = _sluggify_github(heading_query)

    # Find the heading
    start_idx = None
    start_level = None

    heading_re = re.compile(r'^(#{1,6})\s+(.*)\s*$')
    for i, line in enumerate(lines):
        m = heading_re.match(line)
        if not m:
            continue
        level = len(m.group(1))
        text = m.group(2).strip()
        if (text.lower() == heading_query.strip().lower() or
                _sluggify_github(text) == target_slug):
            start_idx = i
            start_level = level
            break

    if start_idx is None:
        return None

    # Collect until next heading of same or higher level
    body_lines = []
    for j in range(start_idx + 1, len(lines)):
        m = heading_re.match(lines[j])
        if m and len(m.group(1)) <= start_level:
            break
        body_lines.append(lines[j])

    # Trim trailing blank lines
    while body_lines and body_lines[-1].strip() == "":
        body_lines.pop()

    return "\n".join(body_lines).strip() or ('section is empty')


def log_readme_section(
        md_path: str,
        heading_query: str,
        log: logging.Logger = logger,
        level: int = logging.INFO) -> bool:
    """
    Extracts a section and writes it to the log line by line.
    Returns true if a section is found and logged, else false.
    """
    content = extract_markdown_section(md_path, heading_query)
    if content is None:
        log.warning(f"README section not found for {heading_query}")
        return False

    border = "-" * 60
    log.log(level, border)
    log.log(level, f'README * {heading_query}')
    log.log(level, border)
    for line in content.splitlines():
        # Avoid empty log lines getting dropped by some handlers.
        log.log(level, line if line.strip() else " ")
    log.log(level, border)
    return True
