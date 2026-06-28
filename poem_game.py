import os
import random

def run_poem_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== COLLABORATIVE POEM GENERATOR ===")
    
    player_input = input("Enter player names separated by commas: ")
    players = [name.strip() for name in player_input.split(",") if name.strip()]
    
    if not players:
        print("No players entered. Exiting.")
        return

    print(f"\nPlayers registered: {players}")

if __name__ == "__main__":
    run_poem_game()