from src.models.match import Match
from src.models.round import Round

def generate_first_round(players):
    # TRIER par rating (DESC)
    sorted_players = sorted(players, key=lambda p: p.rating, reverse=True)
    # Paire 1vs5, 2vs6, 3vs7, 4vs8
    matches = []
    for i in range(0, len(sorted_players), 2):
        p1 = sorted_players[i]
        p2 = sorted_players[i + 4] if i + 4 < len(sorted_players) else sorted_players[i + 1]
        match = Match(p1, p2)
        matches.append(match)
    return matches

def create_round(tournament, round_number):
    round_name = f"Round {round_number}"
    new_round = Round(round_name)
    if round_number == 1:
        matches = generate_first_round(tournament.players)
    else:
        matches = []  # À faire plus tard (rounds suivants)
    for match in matches:
        new_round.add_match(match)
    tournament.add_round(new_round)
    new_round.show()

