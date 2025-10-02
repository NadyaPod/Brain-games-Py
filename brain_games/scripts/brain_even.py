import prompt
from brain_games.cli import welcome_user
from brain_games.scripts.common import win, lose, generate_random_integer


def is_even(num):
    if num % 2 == 0:
        return "yes"
    else:
        return "no"


def single_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    number_to_check = generate_random_integer()
    right_answer = is_even(number_to_check)
    user_answer = prompt.string(f"Question: {number_to_check}\n")

    return (user_answer, right_answer)


def play_game():
    player_name = welcome_user()

    for i in range(3):
        user_answer, right_answer = single_game()

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
