import json
import os

# Define weights
INDIVIDUAL_WEIGHT = 0.39
TEAM_WEIGHT = 0.61

individual_weights = {
    "MVPs": 0.70,
    "DPOYs": 0.04,
    "All_Stars": 0.01,
    "All_NBA_First": 0.04,
    "ROTY": 0.01,
    "Scoring_Titles": 0.10,
    "Assist_Titles": 0.05,
    "Rebound_Titles": 0.05
}

team_weights = {
    "Finals_MVPs": 0.80,
    "Championships": 0.20
}

# Load player data
def load_player_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'players.json')
    with open(data_path, 'r') as f:
        return json.load(f)

players = load_player_data()

# Calculate SGV
def calculate_sgv(stats):
    individual_score = sum(stats.get(k, 0) * individual_weights[k] for k in individual_weights)
    team_score = sum(stats.get(k, 0) * team_weights[k] for k in team_weights)
    final_score = individual_score * INDIVIDUAL_WEIGHT + team_score * TEAM_WEIGHT
    return round(final_score, 3)