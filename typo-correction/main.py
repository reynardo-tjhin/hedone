import math
from re import L
from typing import Any

def measure_distance(letter1: str, letter2: str) -> int:
    """
    Measuring the distance between two letters using Euclidean Distance Method.

    Return -1 if error, otherwise the distance.
    """
    # Check if letters are alphabets
    if ((not letter1.isalpha()) or (not letter2.isalpha())):
        return -1

    # Check if letters are single string
    if ((len(letter1) != 1) and (len(letter2) != 1)):
        return -1

    # keyboard layout
    keyboard = [
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ]
    # Example
    # a: keyboard[1][0]
    # r: keyboard[0][3]
    
    x1 = 0 # x-coordinate for letter1
    y1 = 0 # y-coordinate for letter1
    x2 = 0 # x-coordinate for letter2
    y2 = 0 # y-coordinate for letter2

    # finding the x and y coordinates of both letters
    y = 0
    found_1 = False
    found_2 = False
    for ls in keyboard:

        x = 0
        for char in ls:
            
            # found letter1
            if (char == letter1):
                x1 = x
                y1 = y
                found_1 = True

            # found letter2
            if (char == letter2):
                x2 = x
                y2 = y
                found_2 = True

            x += 1
        
        if (found_1 and found_2):
            break

        y += 1

    # print("{:s} is in keyboard[{:d}][{:d}]".format(letter1, y1, x1))
    # print("{:s} is in keyboard[{:d}][{:d}]".format(letter2, y2, x2))

    # calculate using Euclidean Distance Method
    return math.sqrt(math.pow(math.fabs(y1 - y2), 2) + math.pow(math.fabs(x1 - x2), 2))

def fix_typo(dictionary: Any, typo: str) -> str:
    """
    Fix the typo.
    Idea or Implementation in README.md
    """
    # output
    output = []

    # compare with words of exact length
    len_of_typo = len(typo)
    for w in dictionary[len_of_typo]:
        
        # calculate score
        score = 0
        i = 0
        for letter in typo:
            if (letter != w[i]):
                score += measure_distance(letter, w[i])
            i += 1
        
        output.append((w, score))
    
    # compare with words of non-exact length
    
    # 1. find no of missing letters in each word
    # 2. word must not be greater than half of the length of the word

    # mean the distance for the missing ones (besides)
    
    # rank the output
    i = 0
    while (i < len(output)):
        j = i + 1
        while (j < len(output)):
            if (output[i][1] >= output[j][1]):
                temp = output[i]
                output[i] = output[j]
                output[j] = temp
            j += 1
        i += 1
    
    # temp: print the output
    i = 0
    while (i < 5):
        print(output[i])
        i += 1


# Main
if (__name__ == "__main__"):

    print("Load English Words...")
    
    # open the file containing most of the english words
    file = open("english_words.txt", "r")

    # get the english words and store in data
    data = file.readlines()

    # close the file
    file.close()

    # put the data into a data structure
    # Data Structure: split the words into a dictionary
    # key: length of the word
    # value: list of all the words that are of the key's length
    dictionary = {}
    for word in data:
        
        word = word.strip("\n")
        len_of_word = len(word)

        try:
            dictionary[len_of_word].append(word)
        except (KeyError):
            dictionary[len_of_word] = []
            dictionary[len_of_word].append(word)
    
    # Testing
    fix_typo(dictionary, "prnt")
