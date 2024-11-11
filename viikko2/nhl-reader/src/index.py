from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()
    console.print(Panel.fit("[white] NHL BY NATIONALITY", border_style="cyan"))
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
    nationalities = ["AUS", "AUT", "BLR", "CAN", "CZE", "DEN", "FIN", "GBR", "GER", "LAT", "NOR", "RUS", "SLO", "SUI", "SVK", "SWE", "USA"]
    season = Prompt.ask("Choose season", choices=seasons)
    nationality = Prompt.ask("Choose nationality", choices=nationalities)
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_by_nat(nationality)

    #pelaajataulukko:
    table = Table(title=f"TOP PLAYERS IN {season} FROM {nationality}")
    table.add_column("Name", style="cyan", justify="left")
    table.add_column("Team", style="magenta", justify="center")
    table.add_column("Goals", style="green", justify="center")
    table.add_column("Assists", style="green", justify="center")
    table.add_column("Points", style="green", justify="center")

    print(players)

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))


    console.print(table)

if __name__ == "__main__":
    main()