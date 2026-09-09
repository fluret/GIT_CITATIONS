import argparse
import json
from random import choice

from pyfiglet import figlet_format
from rich import print
from rich.panel import Panel


def charger_citations(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        donnees = json.load(f)

    citations = []
    for item in donnees:
        citations.append((item["text"].strip(), item["author"].strip()))
    return citations


def afficher_citation(citation, auteur):
    print(figlet_format("Citation du jour"))
    print(
        Panel(
            f"[italic gold1]{citation}[/italic gold1]",
            border_style="gold1",
            title=auteur,
            expand=False,
        )
    )


def main():
    parser = argparse.ArgumentParser(
        description="Affiche des citations aléatoires ou listées."
    )
    parser.add_argument(
        "--all", action="store_true", help="Affiche toutes les citations du fichier."
    )
    parser.add_argument(
        "--index", type=int, help="Affiche la citation numéro n (1 pour la première)."
    )
    args = parser.parse_args()

    citations = charger_citations("citations.json")

    if args.all:
        for index, (citation, auteur) in enumerate(citations, start=1):
            print(figlet_format(f"Citation {index}"))
            print(
                Panel(
                    f"[italic gold1]{citation}[/italic gold1]",
                    border_style="gold1",
                    title=auteur,
                    expand=False,
                )
            )
        return

    if args.index is not None:
        if args.index < 1 or args.index > len(citations):
            raise SystemExit(f"L'index doit être compris entre 1 et {len(citations)}.")
        citation, auteur = citations[args.index - 1]
        afficher_citation(citation, auteur)
        return

    citation, auteur = choice(citations)
    afficher_citation(citation, auteur)


if __name__ == "__main__":
    main()
