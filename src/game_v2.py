"""Guess number game
Computer generates the number and will guess it by himself
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Will predict the number by random generator

    Args:
        number (int, optional): The generated number to guess. Defaults to 1.

    Returns:
        int: The number of tries
    """

    count = 0

    while True:
        count += 1

        predict_number = np.random.randint(1, 101)  # assumed number
        if number == predict_number:
            break

    return count


def score_game(random_predict) -> int:
    """Find out average number of the predicts in the argument

    Args:
        random_predict ([type]): function that will guess

    Returns:
        int: average number of predicts
    """

    count_ls = []

    # np.random.seed(1) # seed the generator
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f"The function {random_array.__name__} predicts the numbers in average {score} tries")
    
    return score


# RUN script if files is not impoerted
if __name__ == "__main__":
    score_game(random_predict)
