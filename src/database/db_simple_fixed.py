from datetime import date
from tinydb import TinyDB
from src.models.player import create_player_from_dict
from src.models.tournament import Tournament

db = TinyDB('db.json')

def save_all(all_players, all_tournaments):
    # Sauvegarder joueurs
    players_data = [p.to_dict() for p in all_players]
    db.table('players').truncate()
    db.table('players').insert_multiple(players_data)
    
    # Sauvegarder tournois (simple)
    tour_data = [{'name': t.name} for t in all_tournaments]
    db.table('tournaments').truncate()
    db.table('tournaments').insert_multiple(tour_data)

def load_all():
    all_players = []
    all_tournaments = []
    
    # Charger joueurs
    players_data = db.table('players').all()
    for data in players_data:
        player = create_player_from_dict(data)
        all_players.append(player)
    
    # Charger tournois (simple)
    tours_data = db.table('tournaments').all()
    for data in tours_data:
        t = Tournament(data['name'], "Lieu", date(2024,1,1))
        all_tournaments.append(t)
    
    return all_players, all_tournaments

