#include <stdio.h>
#include "main.h"

int main() {

    // Load the Chemical Names
    printf("Loading the Chemical Names and Symbols...\n");

    load_chemical_symbols("data.txt");

    printf("Hello World!\n");

    return 0;
}

void load_chemical_symbols(char* filename) {
    
    // Open the file
    FILE* fpointer = fopen(filename, "r");



    // Close the file
    fclose(fpointer);
}
