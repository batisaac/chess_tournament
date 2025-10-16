def show_main_menu():
    print("\n" + "="*40)
    print("🏁 GESTIONNAIRE DE TOURNOIS D'ÉCHECS")
    print("="*40)
    print("1. Ajouter un joueur")
    print("2. Créer un tournoi")
    print("3. Voir tous les joueurs")
    print("4. Lancer un tournoi")
    print("5. Modifier classement")
    print("6. Rapports")
    print("0. Quitter")
    print("="*40)

def get_choice():
    while True:
        choice = input("Choisissez (0-6): ")
        if choice in ['0', '1', '2', '3', '4', '5', '6']:
            return int(choice)
        print("❌ Erreur ! Tapez 0, 1, 2, 3, 4, 5 ou 6")

def show_title(title):
    print(f"\n{'='*20} {title} {'='*20}")

def get_string(message):
    return input(f"{message}: ")

def get_number(message):
    while True:
        try:
            return int(input(f"{message}: "))
        except ValueError:
            print("❌ Tapez un nombre !")

def show_players(players):
    print("\n📋 LISTE DES JOUEURS:")
    for i, player in enumerate(players, 1):
        print(f"{i}. {player.first_name} {player.last_name} - {player.rating}")

def show_message(message):
    print(f"\n✅ {message}")

