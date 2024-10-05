from random import randint

class Hangman:
    def __init__(self, words, max_attempts=6) -> None:
        self.words = words
        self.max_attempts = max_attempts
        self.word_to_guess = list(
            map(str.lower, list(words[randint(0, len(words) - 1)]))
        )
        self.current_state = list("_" * len(self.word_to_guess))
        self.used_letters = set()
        self.attempts_left = max_attempts

    def display_current_state(self):
        print(f"\nWord: {' '.join(self.current_state)}")
        print(
            f"Used letters: {', '.join(sorted(self.used_letters)) if self.used_letters else ''}"
        )
        print(f"Remaining attempts: {self.attempts_left}")

    def check_win(self):
        return all(letter in self.current_state for letter in self.word_to_guess)

    def get_valid_guess(self):

        while True:
            guess = input("\nEnter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single alphabetical character.")
            elif guess in self.used_letters:
                print(f"You've already guessed '{guess}'. Try a different letter.")
            else:
                self.used_letters.add(guess)
                return guess

    def update_word_progress(self, guess):
        if guess not in self.word_to_guess:
            return False

        for i, letter in enumerate(self.word_to_guess):
            if letter == guess:
                self.current_state[i] = guess

        return True

    def play(self):
        print("Welcome to Hangman!")
        print(f"The word you have to guess consists of {len(self.word_to_guess)} character.")

        while self.attempts_left > 0:
            self.display_current_state()

            guess = self.get_valid_guess()

            if self.update_word_progress(guess):
                print(f"Good job! '{guess}' is in the word.")
            else:
                self.attempts_left -= 1
                print(f"Sorry, '{guess}' is not in the word.")

            if self.check_win():
                print(f"\nCongratulations! You've guessed the word: {''.join(self.word_to_guess)}")
                break
        else:
            print(f"\nOut of attempts! The word was: {''.join(self.word_to_guess)}. Better luck next time.")


if __name__ == "__main__":
    WORDS = [
        "apple",
        "tiger",
        "chair",
        "pizza",
        "beach",
        "medium",
        "garden",
        "rocket",
        "bridge",
        "dragon",
        "pencil",
    ]

    game = Hangman(WORDS)
    game.play()
