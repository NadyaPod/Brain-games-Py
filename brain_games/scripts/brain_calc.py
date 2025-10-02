import prompt
import random
from brain_games.cli import welcome_user
from brain_games.scripts.common import win, lose, generate_random_integer


def generate_random_operation():
    operations = ["+", "-", "*"]
    return operations[random.randint(0, len(operations) - 1)]


def calculate_expression(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    else:
        print("Unknown operator!")


def single_game(first_number, second_number, operation):
    print("What is the result of the expression?")

    right_answer = calculate_expression(first_number, second_number, operation)
    user_answer = prompt.string(
        f"Question: {first_number} {operation} {second_number}\n"
    )

    return (int(user_answer), right_answer)


def play_game():
    player_name = welcome_user()

    for i in range(3):
        first_number = generate_random_integer()
        second_number = generate_random_integer()
        operation = generate_random_operation()

        while True:
            try:
                user_answer, right_answer = single_game(
                    first_number, second_number, operation
                )
                break
            except ValueError:
                print("Enter number!")
                continue

        if user_answer == right_answer:
            print("Correct!")
        else:
            lose(user_answer, right_answer, player_name)
            return

    win(player_name)


def main():
    # run_tg_bot()
    print("Welcome to the Brain Even!")
    play_game()


if __name__ == "__main__":
    main()
