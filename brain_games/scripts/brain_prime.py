import prompt
from brain_games.scripts.common import play_game


def is_prime(number: int) -> str:
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


def single_game_prime(number_to_check: int, *_) -> tuple[str, str]:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    right_answer = is_prime(number_to_check)
    user_answer = prompt.string(f"Question: {number_to_check}\n")

    if not isinstance(user_answer, str):
        raise ValueError()

    return (user_answer, right_answer)


def main() -> None:
    print("Welcome to the Brain Prime!")
    play_game(3, single_game_prime)
