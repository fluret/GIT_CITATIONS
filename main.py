from random import choice

from pyfiglet import figlet_format
from rich import print
from rich.panel import Panel

with open("citations.txt", "r", encoding="utf-8") as f:
    citations = [line.strip() for line in f if line.strip()]

citation_texte, auteur = choice(citations).rsplit(" - ", 1)

print(figlet_format("Citation du jour"))
print(
    Panel(
        f"[italic gold1]{citation_texte}[/italic gold1]",
        border_style="gold1",
        title=auteur,
        expand=False,
    )
)
