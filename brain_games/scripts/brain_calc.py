import prompt
from brain_games.scripts.common import play_game


def calculate_expression(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    else:
        print("Unknown operator!")


def single_game_calc(first_number, second_number, operation):
    print("What is the result of the expression?")

    right_answer = calculate_expression(first_number, second_number, operation)
    user_answer = prompt.string(
        f"Question: {first_number} {operation} {second_number}\n"
    )

    return (int(user_answer), right_answer)


def main():
    # run_tg_bot()
    print("Welcome to the Brain Even!")
    play_game(3, single_game_calc)
