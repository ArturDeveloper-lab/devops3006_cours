import os
import random
import time

def create_random_number():
    length = random.randint(1, 2)
    return length

def list_on_numbers(length):
    list_random = []
    for i in range(length):
        generate_sequence = random.randint(1, 101)
        list_random.append(generate_sequence)
    return list_random

def show_number_to_user(list_random):
    print(list_random)
    time.sleep(361)
    os.system('clear')

def memory_from_user(list_random):
    list_from_user = []
    numbers_of_num_in_list = len(list_random)
    value_from_user = input(f"Enter a {numbers_of_num_in_list} list of numbers \n")
    result = [int(i) for i in value_from_user.split(",")]
    # list_for_all = list_from_user
    if list_random == result:
        print("True")
    else:
        print("False")

def play():
    random_number = create_random_number()
    list_of_numbers = list_on_numbers(random_number)
    show_number_to_user(list_of_numbers)
    memory_from_user(list_of_numbers)


if __name__ == '__main__':
    play()
# ------------------------------
# list_random = []
# length = random.randint(1, 5)
# for i in range(length):
#     generate_sequence = random.randint(1, 101)
#     list_random.append(generate_sequence)
#
# print(list_random)
# time.sleep(0.7)
# os.system('clear')
#
#
# list_from_user = []
# numbers_of_num_in_list = len(list_random)
# value_from_user = input(f"Enter a {numbers_of_num_in_list} list of numbers \n")
# result = [int(i) for i in value_from_user.split(",")]
# list_for_all = list_from_user
#
# if list_random == result:
#     print("True")
# else:
#     print("False")






