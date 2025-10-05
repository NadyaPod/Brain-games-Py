import prompt
from brain_games.scripts.common import play_game, generate_random_integer


def is_prime(number):
    if number <= 1:
        return "no"
    if number == 2:
        return "yes"
    if number % 2 == 0:
        return "no"
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return "no"
    return "yes"


def single_game_prime(first_number, second_number, *_):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    number_to_check = generate_random_integer()
    right_answer = is_prime(number_to_check)
    user_answer = prompt.string(f"Question: {number_to_check}\n")

    return (user_answer, right_answer)


def main():
    # run_tg_bot()
    print("Welcome to the Brain Prime!")
    play_game(3, single_game_prime)
