import random

def choose_random_word():
    words = ["apple", "banana", "orange", "strawberry", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "*"
    return display

def main():
    word_to_guess = choose_random_word()
    attempts = int(input("Введіть кількість спроб: "))
    guessed_letters = []

    while attempts > 0:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Введіть букву або слово: ").lower()

        if len(guess) == 1:  # Якщо введено лише одну літеру
            if guess in word_to_guess:
                guessed_letters.append(guess)
                print("Ви вгадали літеру!")
            else:
                print("Такої літери немає.")
        else:  # Якщо введено слово
            if guess == word_to_guess:
                print("Вітаємо, ви вгадали слово!")
                break
            else:
                print("Неправильне слово.")

        if set(word_to_guess).issubset(guessed_letters):
            print("Ви вгадали слово!")
            break

        attempts -= 1
        print("Залишилося спроб:", attempts)

    if attempts == 0:
        print("Ви програли. Спроби закінчилися.")

if __name__ == "__main__":
    main()
