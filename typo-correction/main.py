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


def fix_typo(dictionary: Any, typo: str) -> list(('str', int)):
    """
    Return a list of possible corrections for the typo.
    Idea or Implementation in README.md
    """
    # output
    output = []
    output_length = 5 # only output the closest 5 words

    # compare with words of exact length
    len_of_typo = len(typo)
    for w in dictionary[len_of_typo]:

        # calculate score
        dict1 = {}
        dict2 = {}
        score = 0
        i = 0
        for letter in typo:

            # check if any of the letters are different
            if (letter != w[i]):
                score += measure_distance(letter, w[i])

            # to check for misplaced error (for typo)
            if (letter in dict1):
                dict1[letter] += 1
            else:
                dict1[letter] = 1

            # to check for misplaced error (for english word)
            if (w[i] in dict2):
                dict2[w[i]] += 1
            else:
                dict2[w[i]] = 1
            
            i += 1
        
        # misplaced error
        if (dict1 == dict2):
            score = 0
        
        # append to output (only 5 closest are added)
        output.append((w, score))
        output = sorted(output, key=lambda output: output[1])
        if (len(output) == output_length + 1):
            output.pop()
    
    return output


def advanced_fix_typo(dictionary: Any, typo: str) -> list('str'):
    """
    Includes other words that are not the same length.
    """
    #TODO (second version)

    # compare with words of non-exact length
    half_len_of_typo = int(len(typo) / 2)
    # length of typo +/- half_len_of_typo
    i = 0
    while (i < len(typo)):
        
        length = len(typo) - half_len_of_typo + i
        for w in dictionary[length]:
            
            # calculate score
            dict1 = {}
            dict2 = {}
            score = 0
            j = 0
            # TODO

        i += 1
    
    # 1. find no of missing letters in each word
    # 2. word must not be greater than half of the length of the word

    # mean the distance for the missing ones (besides)

# Main
if (__name__ == "__main__"):

    print("Load English Words...")
    print()
    
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

        if (len_of_word in dictionary):
            dictionary[len_of_word].append(word)
        else:
            dictionary[len_of_word] = [word]
    
    # get input and output result
    user_input = ""
    while (True):
        
        user_input = input("Input: ")
        if (user_input == "end"):
            print("Program exits.")
            break

        # Testing
        result = fix_typo(dictionary, user_input)

        # output
        print("Did you mean?")
        i = 1
        for w in result:
            print("{:d}. {:s}, score = {:.2f}".format(i, w[0], w[1]))
            i += 1
        print()
