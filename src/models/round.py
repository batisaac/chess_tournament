from datetime import datetime

class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_time = str(datetime.now())
        self.end_time = None

    def add_match(self, match):
        self.matches.append(match)

    def end_round(self):
        self.end_time = str(datetime.now())

    def show(self):
        print(f"\n=== {self.name} ===")
        print(f"Début: {self.start_time}")
        if self.end_time:
            print(f"Fin: {self.end_time}")
        for match in self.matches:
            match.show()

