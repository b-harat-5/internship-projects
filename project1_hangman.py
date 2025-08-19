import random

def hangman():
    # Predefined words
    words = ["python", "github", "intern", "project", "simple"]
    word = random.choice(words)  # Pick a random word
    guessed = []  # Correct letters guessed
    wrong_guesses = 0
    max_guesses = 6

    print("🎯 Welcome to Hangman!")
    print("_ " * len(word))  # Show blanks

    while wrong_guesses < max_guesses:
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue

        if guess in guessed:
            print("⚠️ You already guessed that letter.")
            continue

        if guess in word:
            print("✅ Good guess!")
            guessed.append(guess)
        else:
            print("❌ Wrong guess.")
            wrong_guesses += 1

        # Display current progress
        current_word = ""
        for letter in word:
            if letter in guessed:
                current_word += letter + " "
            else:
                current_word += "_ "
        print(current_word)

        # Check if the word is guessed
        if all(letter in guessed for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
