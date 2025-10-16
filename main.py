from src.views.menu import show_main_menu, get_choice, show_players
from src.controllers.player_controller import add_player, modify_rating
from src.controllers.tournament_controller import create_tournament, add_players_to_tournament
from src.controllers.swiss_system import create_round
from src.database.db_simple import save_all, load_all

# CHARGER DONNÉES
all_players, all_tournaments = load_all()

while True:
    show_main_menu()
    choice = get_choice()
    
    if choice == 1:
        add_player(all_players)
    elif choice == 2:
        create_tournament(all_tournaments)
    elif choice == 3:
        show_players(all_players)
    elif choice == 4:
        if all_tournaments:
            print(f"Tournoi: {all_tournaments[-1].name}")
            add_players_to_tournament(all_tournaments[-1], all_players)
            create_round(all_tournaments[-1], 1)
        else:
            print("❌ Créez un tournoi d'abord !")
    elif choice == 5:
        modify_rating(all_players)
    elif choice == 0:
        save_all(all_players, all_tournaments)
        print("👋 Au revoir ! Données sauvegardées.")
        break