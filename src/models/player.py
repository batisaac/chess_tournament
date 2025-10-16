from datetime import date

class Player:
    def __init__(self, last_name, first_name, birth_date, gender, rating):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date  # date(2000, 1, 1)
        self.gender = gender
        self.rating = rating
        self.score = 0.0

    def show(self):
        print(f"{self.first_name} {self.last_name} - Rating: {self.rating} - Score: {self.score}")

    def to_dict(self):
        # Simple dict pour sauvegarde
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': str(self.birth_date),
            'gender': self.gender,
            'rating': self.rating,
            'score': self.score
        }

def create_player_from_dict(data):
    # Fonction simple pour recréer un joueur
    birth = date.fromisoformat(data['birth_date'])
    player = Player(data['last_name'], data['first_name'], birth, data['gender'], data['rating'])
    player.score = data['score']
    return player

