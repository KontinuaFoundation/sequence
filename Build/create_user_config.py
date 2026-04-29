import json
from pathlib import Path

cfg = {
    "Languages": ["en_US"],
    "Paper": "Letter",
    "LatexExecutable": "lualatex",
}
out = Path(__file__).parent / "user.cfg"
out.write_text(json.dumps(cfg, indent=2), encoding="utf-8")
print(f"Created {out}")
