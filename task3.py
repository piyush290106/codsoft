import random

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock / paper / scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "user"
    return "computer"

def main():
    print("===== ROCK - PAPER - SCISSORS GAME =====")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose     : {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("Result: It's a tie 🤝")
        elif result == "user":
            print("Result: You WIN 🎉")
            user_score += 1
        else:
            print("Result: Computer WINS 💻")
            computer_score += 1

        print(f"\nScoreboard:")
        print(f" You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
