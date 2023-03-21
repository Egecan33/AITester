import random
import os


class LearningAI:
    def __init__(self, data_file):
        self.data_file = data_file
        if os.path.exists(data_file):
            with open(data_file, "r") as f:
                self.choices = list(map(int, f.readline().split(",")))
        else:
            self.choices = [1, 2, 3]

    def make_choice(self):
        choice = random.choice(self.choices)
        print(f"AI chose {choice} based on its previous learning.")
        return choice

    def learn_from_choice(self, choice):
        self.choices.append(choice)

    def save_data(self):
        with open(self.data_file, "w") as f:
            f.write(",".join(map(str, self.choices)))

    def print_choice_frequencies(self):
        choice_counts = {1: 0, 2: 0, 3: 0}
        for choice in self.choices:
            choice_counts[choice] += 1

        total_choices = len(self.choices)
        print("AI choice frequencies:")
        print(
            f"Rock: {choice_counts[1]} ({choice_counts[1] / total_choices * 100:.2f}%)"
        )
        print(
            f"Paper: {choice_counts[2]} ({choice_counts[2] / total_choices * 100:.2f}%)"
        )
        print(
            f"Scissors: {choice_counts[3]} ({choice_counts[3] / total_choices * 100:.2f}%)"
        )


class LearningAIGame:
    def __init__(self):
        self.ai = LearningAI("ai_data.txt")

    def play(self):
        print("Welcome to the Learning AI Game!")

        while True:
            choice = int(input("Enter your choice (1: Rock, 2: Paper, 3: Scissors): "))

            ai_choice = self.ai.make_choice()

            # Explain AI's choice
            choice_mapping = {1: "Rock", 2: "Paper", 3: "Scissors"}
            print(f"AI chose {choice_mapping[ai_choice]}")

            self.ai.learn_from_choice(ai_choice)

            # Print choice frequencies
            self.ai.print_choice_frequencies()

            if choice == ai_choice:
                print("Tie!")
            elif (
                (choice == 1 and ai_choice == 3)
                or (choice == 2 and ai_choice == 1)
                or (choice == 3 and ai_choice == 2)
            ):
                print("You win!")
            else:
                print("You lose!")

            save = input("Do you want to save the AI's learning progress? (y/n): ")
            if save.lower() == "y":
                self.ai.save_data()

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != "y":
                break


if __name__ == "__main__":
    game = LearningAIGame()
    game.play()
