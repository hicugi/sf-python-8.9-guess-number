# Project 0. Guess number

## Contents

1. [Description](README.md#Description)
2. [For what?](README.md#for-what)
3. [Short information about data](README.md#Short-information-about-data)
4. [Stages of work on the project](README.md#Stages-of-work-on-the-project)
5. [Results](README.md#Results)
6. [Conclusion](README.md#Conclusion)

### Description

Script that will guess a random number with a less attempts.

### For what?

Home work for [SkillFactory](https://skillfactory.ru/).
Have to write the program, that will guess the number with less attempt.

**Conditions:**

- Computer will generate number between 0 to 100 and we have to find out which number is it. `find out` means - write a progrma, that will guess the number.
- Algorithm will check - is the number is more or less of our guess

**Quality metric**
Results will be measured as average of 1000th attempts

**What we will practice**
Learning to write good code in Python

### Short information about data

#### [First version](src/game.py)

Works automatically and predicts the number in a stupid way (will count from 1 to 100 until find out the answer).

#### [Second version](src/game_v2.py)

- `random_predic`: function that has one argument (integer) which predict the number by random between 1 to 1000
- `score_game`: function that has one argument (function) which find out average number of the predicts in the argument
- `dumb_predic`: function that has one argument (integer) which predict the number by counting from 1 to 100
- `smart_predict`: function that has one argument (integer) which predict the number in a Ninja way

### Stages of work on the project

1. Translate Russian texts to English
2. Creat function `smart_predict` in [game_v2](src/game_v2.py)
3. Export `requirements.txt` for python libraries for [PIP](https://pypi.org/project/pip/)
4. Export `environment.yml` for [Anaconda](https://www.anaconda.com/) environment
5. Update [presentation](src/game.ipynb) for [Jupyter Notebook](https://jupyter.org/)

### Results:

`smart_predict` should predict the number less than a 20 tries

### Conclusion:

You can see presentation with [Jupyter Notebook](https://jupyter.org/) **[here](game.ipynb)**

:arrow\*up:[go to contents](#)

If information about this project may seems interesting to you, I will be happy if you click on ⭐️ for me <3
