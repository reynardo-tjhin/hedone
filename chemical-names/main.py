from re import A, L
from attr import has
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

        #####################################################
        # Implementation Idea:                              #
        # Using a stack of stacks                           #
        #####################################################

        # Iterate each character
        stack = []
        has_added = True
        output_length = 0
        i = 0
        while (True):

            # first step: get all the possible subwords 
            # and append them to a smaller stack
            smaller_stack = []
            if (has_added):
                w = ""
                for j in range(1, max_symbol_len + 1):
                    w = word[i:i+j]
                    smaller_stack.append(w)
                stack.append(smaller_stack)
            
            # second step: pop subword inside the smaller stack
            try:
                top = stack[ len(stack) - 1 ].pop()

            except (IndexError):

                if (len(stack) != 0):
                    stack.pop()
                else:
                    output = []
                    break

            # third step: find the chemical symbol
            try:
                # found the chemical
                chemical = periodic_table[top.lower()]

                # update output length, output and i
                output_length += len(chemical.get_symbol())
                output.append(chemical)
                i += len(chemical.get_symbol())

                # update has_added
                has_added = True

            except (KeyError):

                # chemical symbol not found
                has_added = False

                # no more possible within the substack (or smaller stack)
                if (len(stack[ len(stack) - 1 ]) == 0):
                    
                    # no more output => cannot go backtrack => no more output
                    if (len(output) == 0):
                        break

                    # remove the most recent chemical
                    rmv = output.pop()

                    # update output length and i
                    i -= len(rmv.get_symbol())
                    output_length -= len(rmv.get_symbol())

            # output length is the same as length of word => done
            if (output_length >= len(word)):
                break

    # Output the result
    print("Output:")
    for chemical in output:
        print("{:s}: {:s}".format(chemical.get_symbol(), chemical.get_name()))
    print()