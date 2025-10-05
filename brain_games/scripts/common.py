import random
import math
from brain_games.cli import welcome_user
from typing import Callable


def win(player_name: str) -> None:
    print(f"Congratulations, {player_name}!")


def lose(user_answer: str | int, right_answer: str | int, player_name: str) -> None:
    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{right_answer}'.\n"
        f"Let's try again, {player_name}!",
    )


def generate_random_integer() -> int:
    return math.floor(random.uniform(0.1, 1) * 100)


def generate_random_integer_range(start: int, stop: int) -> int:
    return random.randint(start, stop)


def generate_random_operation() -> str:
    operations = ["+", "-", "*"]
    return operations[random.randint(0, len(operations) - 1)]


def play_game(rounds: int, single_game: Callable) -> None:
    player_name = welcome_user()

    for i in range(rounds):
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
