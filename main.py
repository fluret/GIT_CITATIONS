from random import choice

from pyfiglet import figlet_format
from rich import print

with open("citations.txt", "r", encoding="utf-8") as f:
    citations = f.readlines()

citations = [c.strip() for c in citations]
citation = choice(citations)

print(figlet_format("Citation"))
print(f"[cyan]{citation}[/cyan]")
