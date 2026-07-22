import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SITE_DIR = BASE_DIR / "site"
DATA_DIR = BASE_DIR / "src" / "data"
TEMPLATES_DIR = BASE_DIR / "src" / "generator" / "templates"


def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def rel_root(output_path: Path) -> str:
    depth = len(output_path.relative_to(SITE_DIR).parent.parts)
    if depth == 0:
        return ""
    return "/".join([".."] * depth)


def generate() -> None:
    livro = load_json(DATA_DIR / "livro.json")

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    env.globals["type"] = type

    output_path = SITE_DIR / "index.html"
    template = env.get_template("pages/index.html")
    html = template.render(livro=livro, root_path=rel_root(output_path))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✓ {output_path.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    generate()
