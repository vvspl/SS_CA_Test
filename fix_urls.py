from pathlib import Path
import re

path = Path(r"d:\Nova IT\20. Raif CardActivationCheck\Mock JSON on Github\SS_CA_Test\v2\card-management\cards.json")
text = path.read_text(encoding="utf-8")
text, count = re.subn(r'("uri":)\s*(https://[^\s,}]+)', r'\1 "\2"', text)
path.write_text(text, encoding="utf-8")
print(f"updated {count} occurrences")
