"""Guess number game
Computer generates the number and will guess it by himself
"""

import numpy as np


def random_generate(**args):
    """Random int generator

    Args:
        size: sizeint or tuple of ints, optional
              Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. Default is None, in which case a single value is returned.

    Returns:
        int or ndarray of ints: size-shaped array of random integers from the appropriate distribution, or a single such random int if size not provided.
    """
    return np.random.randint(1, 101, **args)


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

        predict_number = random_generate() # assumed number
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
    random_array = random_generate(size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f"The function {random_predict.__name__} predicts the numbers in average {score} tries")
    
    return score


# RUN script if files is not impoerted
if __name__ == "__main__":
    score_game(random_predict)
