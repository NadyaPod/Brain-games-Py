import random
import math


def win(player_name):
    print(f"Congratulations, {player_name}!")


def lose(user_answer, right_answer, player_name):
    print(
        f"""'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {player_name}!"""
    )


def generate_random_integer():
    return math.floor(random.uniform(0.1, 1) * 100)
