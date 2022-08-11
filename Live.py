
def welcome(a):
    name = a
    print(f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play.")
    return name


def load_game():
    choose_a_game_to_play = int(
        input("Please choose a game to play:\n 1. Memory Game - a sequence of numbers will appear "
              "for 1 second and you have to guess it back\n "
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
    choose_game_difficulty = int(input("choose game difficulty from 1 to 5: "))
    if (3 > choose_a_game_to_play > 0)\
            and (choose_game_difficulty < 5 or choose_game_difficulty > 0):
        print(f"The selected game is {choose_a_game_to_play} and the level of difficulty is {choose_game_difficulty}")
    else:
        print(f"The selected game is unavailable and the level of difficulty is unavailable too")






