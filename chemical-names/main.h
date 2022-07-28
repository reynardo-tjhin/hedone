#ifndef MAIN_H
#define MAIN_H

#define MAX_CHEMICAL_SYMBOL 4
#define MAX_CHEMICAL_NAME 100

// Data structure
typedef struct chemical {
    int atomic_number;
    char symbol[MAX_CHEMICAL_SYMBOL];
    char name[MAX_CHEMICAL_NAME];
    double atomic_mass;
} chemical;

// Function Declarations
void load_chemical_symbols(char* filename);
int main();

#endif