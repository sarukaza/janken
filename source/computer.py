import random

def pon():
    choices = ["グー", "チョキ", "パー"]
    return random.choice(choices)


computer_choice = get_computer_janken_choice()
print(f"コンピュータの手: {computer_choice}")
