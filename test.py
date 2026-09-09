from random import choice

from rich import print
from rich.panel import Panel
from rich_pyfiglet import RichFiglet

with open("citations.txt", "r", encoding="utf-8") as f:
    citations = f.readlines()

citations = [c.strip() for c in citations]
citation = choice(citations)

rich_fig = RichFiglet(
    "Citation du jour",
    font="ansi_shadow",
    colors=["#ff0000", "bright_blue"],
)

print(rich_fig)
print(
    Panel(
        f"[italic gold1]« {citation} »[/italic gold1]",
        border_style="gold1",
        expand=False,
    )
)
