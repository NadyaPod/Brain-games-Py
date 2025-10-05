import prompt
from brain_games.scripts.common import play_game, generate_random_integer_range


def single_game_progression(first_number: int, *_) -> tuple[str, str]:
    print("What number is missing in the progression?")

    step = generate_random_integer_range(1, 10)
    progression_len = generate_random_integer_range(5, 11)
    progression_start = first_number

    progression = []

    for i in range(0, progression_len * step, step):
        progression.append(str(progression_start + i))

    index_to_hide = generate_random_integer_range(0, progression_len - 1)
    right_answer = progression[index_to_hide]
    progression[index_to_hide] = ".."

    user_answer = prompt.string(f"Question: {' '.join(progression)}\n")

    if not isinstance(user_answer, str):
        raise ValueError()

    return (user_answer, right_answer)


def main() -> None:
    print("Welcome to the Brain Progression!")
    play_game(3, single_game_progression)
