from src.models.tournament import Tournament
from src.views.menu import get_string, get_number, show_message
from datetime import date

def create_tournament(all_tournaments):
    print("\n🏆 CRÉER UN TOURNOI")
    name = get_string("Nom du tournoi")
    location = get_string("Lieu")
    year = get_number("Année")
    
    tournament = Tournament(name, location, date(year, 10, 15))
    all_tournaments.append(tournament)
    show_message(f"Tournoi '{name}' créé !")

def add_players_to_tournament(tournament, all_players):
    print(f"\n👥 AJOUTER JOUEURS À {tournament.name}")
    show_players_list(all_players)
    print("Tapez 0 pour arrêter")
    
    while True:
        choice = get_number("Numéro joueur (0=stop)")
        if choice == 0:
            break
        if 1 <= choice <= len(all_players):
            player = all_players[choice - 1]
            if player not in tournament.players:
                tournament.add_player(player)
                print(f"✅ {player.first_name} ajouté")
        else:
            print("❌ Numéro invalide")

def show_players_list(players):
    for i, p in enumerate(players, 1):
        print(f"{i}. {p.first_name} {p.last_name} - {p.rating}")

