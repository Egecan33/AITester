import java.util.Scanner;

public class LearningAIGame {

    private Scanner scanner;
    private LearningAI ai;

    public LearningAIGame() {
        scanner = new Scanner(System.in);
        ai = new LearningAI("ai_data.txt");
    }

    public void play() {
        System.out.println("Welcome to the Learning AI Game!");

        while (true) {
            // Ask the player for their choice
            System.out.print("Enter your choice (1, 2, or 3): ");
            int choice = scanner.nextInt();

            // Make the AI's choice and learn from it
            int aiChoice = ai.makeChoice();
            ai.learnFromChoice(aiChoice);

            // Determine the outcome and print it
            if (choice == aiChoice) {
                System.out.println("Tie!");
            } else if ((choice == 1 && aiChoice == 3) || (choice == 2 && aiChoice == 1)
                    || (choice == 3 && aiChoice == 2)) {
                System.out.println("You win!");
            } else {
                System.out.println("You lose!");
            }
        }
    }

    public static void main(String[] args) {
        LearningAIGame game = new LearningAIGame();
        game.play();
    }
}
