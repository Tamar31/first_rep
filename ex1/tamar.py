import random
# import colorama
from colorama import Fore


def select_word():

    """

    :return: a 5 letters random word from the words list
    """

    with open("words.txt") as words:
        words = words.read()
        words_split = words.split("\n")
        index = random.randint(0, len(words_split))
        selected_word = words_split[index]
        return selected_word


def tester(selected_word):

    """

    :param selected_word: the selected word that the gamer try to guess
    :return: result of your guess, your guess with different color for each letter
    """

    guess_word = input(Fore.LIGHTWHITE_EX + "Please enter your guess, a 5 letters word: ")

    with open("words.txt") as words:
        words = words.read()
        words_split = words.split("\n")

    while len(guess_word) != 5 or guess_word not in words_split:
        if len(guess_word) != 5:
            print("It isn't a 5 letters word")
            guess_word = input(Fore.LIGHTWHITE_EX + "Please enter your guess, a 5 letters word: ")

        else:
            print("It isn't a word")
            guess_word = input(Fore.LIGHTWHITE_EX + "Please enter your guess, a 5 letters word: ")

    copy_selected_word = selected_word
    green_cuont = 0

    for i in range(len(guess_word)):
        letter = guess_word[i]
        if guess_word[i] == copy_selected_word[i]:
            print(Fore.GREEN + guess_word[i], end="")
            copy_selected_word = copy_selected_word.replace(letter, "0", 1)
            green_cuont += 1

        elif guess_word[i] in copy_selected_word:
            print(Fore.YELLOW + guess_word[i], end="")
            copy_selected_word = copy_selected_word.replace(letter, "0", 1)


        else:
            print(Fore.BLACK + guess_word[i], end="")

    if green_cuont == 5:
        print("")
        print(Fore.LIGHTWHITE_EX + "You won!!!")
        return False
    else:
        True




if __name__ == '__main__':

    selected_word = select_word()
    count = 0
    while count < 6:
        if (tester(selected_word)) == False:
            break
        count += 1
        print("")

    if count == 6:
        print(Fore.LIGHTWHITE_EX + "You lost :( ")
        print("the word was " + selected_word)
