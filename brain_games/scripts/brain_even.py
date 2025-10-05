import prompt
from brain_games.scripts.common import generate_random_integer, play_game


def is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def single_game_even(*_):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number_to_check = generate_random_integer()
    right_answer = is_even(number_to_check)
    user_answer = prompt.string(f"Question: {number_to_check}\n")

    return (user_answer, right_answer)


def main():
    # run_tg_bot()
    print("Welcome to the Brain Even!")
    play_game(3, single_game_even)
