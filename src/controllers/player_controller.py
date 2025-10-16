from src.models.player import Player
from src.views.menu import get_string, get_number, show_message
from datetime import date

def add_player(all_players):
    print("\n➕ AJOUTER UN JOUEUR")
    last_name = get_string("Nom")
    first_name = get_string("Prénom")
    birth_year = get_number("Année naissance")
    gender = get_string("Sexe (M/F)")
    rating = get_number("Classement")
    
    player = Player(last_name, first_name, date(birth_year, 1, 1), gender, rating)
    all_players.append(player)
    show_message(f"{first_name} {last_name} ajouté !")

def modify_rating(all_players):
    print("\n🔧 MODIFIER CLASSEMENT")
    show_players_list(all_players)
    index = get_number("Numéro joueur") - 1
    if 0 <= index < len(all_players):
        new_rating = get_number("Nouveau classement")
        all_players[index].rating = new_rating
        show_message("Classement mis à jour !")
    else:
        print("❌ Joueur introuvable")

def show_players_list(players):
    for i, p in enumerate(players, 1):
        print(f"{i}. {p.first_name} {p.last_name} - {p.rating}")

