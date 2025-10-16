class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0.0
        self.score2 = 0.0

    def set_result(self, result):
        # 1 = player1 gagne, 2 = player2 gagne, 0 = nul
        if result == 1:
            self.score1 = 1.0
            self.score2 = 0.0
        elif result == 2:
            self.score1 = 0.0
            self.score2 = 1.0
        else:
            self.score1 = 0.5
            self.score2 = 0.5
        
        self.player1.score += self.score1
        self.player2.score += self.score2

    def show(self):
        print(f"{self.player1.first_name} {self.score1} vs {self.player2.first_name} {self.score2}")

