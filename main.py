import game_data
import art
import random
import os

def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

def start_game():
    print(art.logo)
    data = game_data.data
    score = 0
    subject_used = []
    

    subject1 = random.choice(data)
    while True:
        
        filtered_data = [item for item in data if item not in subject_used]
        subject2 = random.choice(filtered_data)

        print(f"Compare A: {subject1['name']}, a {subject1['description']}, from {subject1['country']}")
        print(art.vs)
        print(f"Against B: {subject2['name']}, a {subject2['description']}, from {subject2['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ")
        if choice == 'A':
            if subject1['follower_count'] > subject2['follower_count']:
                subject_used.append(subject1)
                score += 1
                subject1 = subject2
                clear_console()
                print(f'You are right! Current score: {score}')
            else:
                clear_console()
                print(f'Sorry, wrong answer. Final score: {score}')
                return
        elif choice == 'B':
            if subject2['follower_count'] > subject1['follower_count']:
                score += 1
                subject_used.append(subject2)
                subject1 = subject2
                clear_console()
                print(f'You are right! Current score: {score}')
            else:
                clear_console()
                print(f'Sorry, wrong answer. Final score: {score}')
                return

start_game()
