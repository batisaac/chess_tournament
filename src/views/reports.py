from src.views.menu import show_title

def show_all_players_alpha(players):
    show_title("JOUEURS PAR ORDRE ALPHABÉTIQUE")
    sorted_players = sorted(players, key=lambda p: p.last_name)
    for player in sorted_players:
        player.show()

def show_all_players_rating(players):
    show_title("JOUEURS PAR CLASSEMENT")
    sorted_players = sorted(players, key=lambda p: p.rating, reverse=True)
    for player in sorted_players:
        player.show()

def show_tournaments(tournaments):
    show_title("TOUS LES TOURNOIS")
    for i, tour in enumerate(tournaments, 1):
        print(f"{i}. {tour.name} - {tour.location}")

def show_rounds(tournament):
    show_title(f"ROUNDS DE {tournament.name}")
    for round_obj in tournament.rounds:
        round_obj.show()

