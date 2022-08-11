import random


def secret_number():
    return random.randint(1, 100)


def difficult_num_from_user():
    return int(input("Enter a number between 1 - 100: \n"))


def play():
    if secret_number() == difficult_num_from_user():
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    play()
