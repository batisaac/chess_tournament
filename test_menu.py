from src.views.menu import show_main_menu, get_choice, show_players
from src.models.player import Player
from datetime import date

# Créer 2 joueurs pour tester
players = [
    Player("Dupont", "Jean", date(1990,1,1), "M", 1500),
    Player("Martin", "Paul", date(1985,5,5), "M", 1800)
]

# Test menu
show_main_menu()
choice = get_choice()
print(f"Vous avez choisi: {choice}")

# Test affichage joueurs
show_players(players)