from datetime import date

class Tournament:
    def __init__(self, name, location, date_start, num_rounds=4):
        self.name = name
        self.location = location
        self.date_start = date_start  # date(2023, 10, 15)
        self.num_rounds = num_rounds
        self.players = []
        self.rounds = []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_obj):
        self.rounds.append(round_obj)

    def show(self):
        print(f"\n=== {self.name} ===")
        print(f"Lieu: {self.location} - Date: {self.date_start}")
        print("Joueurs:")
        for player in self.players:
            player.show()

    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'date_start': str(self.date_start),
            'num_rounds': self.num_rounds,
            'player_names': [f"{p.first_name} {p.last_name}" for p in self.players]
        }

