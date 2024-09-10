import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 10  # Ограничиваем количество попыток до 10

    print("Я загадал число от 1 до 100.")
    print(f"У вас есть {attempts} попыток, чтобы угадать его.")

    for attempt in range(attempts):
        guess = input(f"Попытка {attempt + 1}. Введите ваше предположение: ")

        # Проверяем, введено ли число
        if not guess.isdigit():
            print("Пожалуйста, введите корректное число.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Пожалуйста, выбирайте число в диапазоне от 1 до 100.")
        elif guess < number_to_guess:
            print("Слишком маленькое число!")
        elif guess > number_to_guess:
            print("Слишком большое число!")
        else:
            print(f"Поздравляем! Вы угадали число {number_to_guess}!")
            break
    else:
        print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

# Запускаем игру
guess_number_game()
