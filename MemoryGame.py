import os
import random
import time

list_random = []
length = random.randint(1, 5)
for i in range(length):
    generate_sequence = random.randint(1, 101)
    list_random.append(generate_sequence)

print(list_random)
time.sleep(0.7)
os.system('clear')


list_from_user = []
numbers_of_num_in_list = len(list_random)
value_from_user = input(f"Enter a {numbers_of_num_in_list} list of numbers \n")
result = [int(i) for i in value_from_user.split(",")]
list_for_all = list_from_user

if list_random == result:
    print("True")
else:
    print("False")









