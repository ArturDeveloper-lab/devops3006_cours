import random
import os
from world_of_game.score import calculate_points_of_winning
from world_of_game.utils import SCORES_FILE_NAME


def secret_number():
    return random.randint(1, 1)


def difficult_num_from_user():
    return int(input("Enter a number between 1 - 100: \n"))


def play():
    difficult_number = difficult_num_from_user()
    if secret_number() == difficult_number:
        # file = open(SCORES_FILE_NAME, 'w+')
        # file.write(str(0))
        POINTS_OF_WINNING = (calculate_points_of_winning(difficult_number))
        file = open(SCORES_FILE_NAME, 'r+')
        score_from_file = int(file.read())

        total_score = int(POINTS_OF_WINNING) + score_from_file
        file = open(SCORES_FILE_NAME, 'w+')
        file.write(str(total_score))
        return total_score

    else:
        print("False")


if __name__ == '__main__':
    play()
