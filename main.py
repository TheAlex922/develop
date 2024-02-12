import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "*"
    return displayed_word

def game():
    word = choose_word()
    attempts = int(input("Введіть кількість спроб вгадати: "))
    guessed_letters = []

    while attempts > 0:
        print(display_word(word, guessed_letters))

        guess = input("Введіть літеру або слово: ").lower()

        if guess == word:
            print("Ви вгадали слово!")
            break
        elif len(guess) == 1:
            if guess in guessed_letters:
                print("Ви уже вводили цю літеру!")
            elif guess in word:
                guessed_letters.append(guess)
                print("Ця літера є в слові!")
            else:
                print("Такої літери немає!")
            attempts -= 1
        else:
            print("Спробуйте ще раз!")

        if "*" not in display_word(word, guessed_letters):
            print("Ви вгадали слово!")
            break

    if attempts == 0:
        print("Ви програли! Слово було:", word)

if __name__ == "__main__":
    game()