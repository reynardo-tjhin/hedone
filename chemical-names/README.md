# Input to Chemical Symbols

This repository aims to take in an input from user and turns the input into a string of chemical symbols.

## Examples
1. Input: boy <br>
Output: <br>
B: Boron <br>
O: Oxygen <br>
Y: Yttrium <br>

2. Input: win <br>
Output: <br>
W: Tungsten <br>
In: Indium <br>

3. Input: test <br>
Output: <br>

## How It Works

Input: honey
Output: Ho Ne Y (Holmium Neon Yttrium)

1. Get the maximum length of the chemical symbols
maximum length = 3

2. Get the first 3 subwords of "honey"
subwords = ["h", "ho", "hon"]
stack = [ ["h", "ho", "hon"] ]

3. Pop the subword of the last element of the stack
subword = "hon"
Check the chemical symbol
If no, pop another one
subword = "ho" for Holmium
Add the chemical symbol in the output

4. Get the next 3 subwords after "ho"
subwords = ["n", "ne", "ney"]
stack = [ ["h"], ["n", "ne", "ney"] ]

5. Repeat steps 3 and 4