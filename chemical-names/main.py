from re import L
from numpy import char
import pandas as pd

# Create a class of Chemical
class Chemical:

    # Initializing the object
    def __init__(self, atomic_number, symbol, name, atomic_mass):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.name = name
        self.atomic_mass = atomic_mass

    # Getter Methods
    def get_atomic_number(self):
        return self.atomic_number

    def get_symbol(self):
        return self.symbol
    
    def get_name(self):
        return self.name

    def get_atomic_mass(self):
        return self.atomic_mass

# Main Function
if (__name__ == "__main__"):
    
    # Get the file
    data = pd.read_csv("data.txt", sep='\t', header=None)

    number_of_chemicals = len(data)
    print("There are {:d} chemicals obtained from data.".format(number_of_chemicals))

    # Put the chemicals into a single dictionary
    periodic_table = {}
    max_symbol_len = 0
    for i in range(0, number_of_chemicals):

        # Store the new chemical
        atomic_number = int(data.values[i, 0])
        symbol = data.values[i, 1].strip(" ")
        name = data.values[i, 2].strip(" ")
        atomic_mass = data.values[i, 3]
        new_chemical = Chemical(atomic_number, symbol, name, atomic_mass)

        # Store the Chemical Name and Symbol in the Dictionary
        periodic_table[symbol.lower()] = new_chemical

        # Update the maximum symbol length
        if (max_symbol_len < len(symbol)):
            max_symbol_len = len(symbol)

    # Get the user input
    user_input = input("Input: ").lower()

    # Iterate each word
    output = []
    for word in user_input.split(sep=" "):

        # Iterate each character
        character = ""
        i = 0
        j = 1
        while (i < len(word)):
            
            for k in range(0, j):
                character += word[i + k]

            print("{:d}: {:s}".format(i, character))

            try:
                # finding the chemical symbol
                output.append(periodic_table[character])
                # update i
                i += 1
                # update j
                j = 1
                # update character
                character = ""

                continue

            # when key not found
            except KeyError:

                if (len(character) >= max_symbol_len):

                    # get the recent symbol
                    recent_symbol = Chemical(0, "", "", 0)
                    if (len(output) != 0):

                        recent_symbol = output.pop()
                        # update the i
                        i -= (len(recent_symbol.get_symbol()) + max_symbol_len)
                        # update j
                        j += 1
                        # update character
                        character = ""
                    
                    else:
                        print("{:s} does not have the chemical symbols.".format(word))
                        break
                
                if (i < -1):
                    print("{:s} does not have the chemical symbols.".format(word))
                    break

            i += 1

    # Output the result
    print("Output:")
    for chemical in output:
        print("{:s}: {:s}".format(chemical.get_symbol(), chemical.get_name()))
    print()