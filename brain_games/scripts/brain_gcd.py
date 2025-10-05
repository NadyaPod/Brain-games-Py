import prompt
from brain_games.scripts.common import play_game


def single_game_gcd(first_number, second_number, *_):
    print("Find the greatest common divisor of given numbers.")
    user_answer = prompt.string(f"Question: {first_number} {second_number}\n")

    while second_number:
        temp = second_number
        second_number = first_number % second_number
        first_number = temp

    right_answer = first_number

    return (int(user_answer), right_answer)


def main():
    # run_tg_bot()
    print("Welcome to the Brain GCD!")
    play_game(3, single_game_gcd)
