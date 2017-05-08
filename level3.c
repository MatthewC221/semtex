/* 

* UPDATE: This takes too long for strings over 11, I can't guarantee the length 
* to be 6-11, therefore I made a different program in Python

* Brute force semtex level3!!! Numbers 1-8 
* We should try from 6 characters upwards (minimum 6 until we lock1 = 400
* Try until 15?
* Permutations are easy to calculate. (8)^6, (8)^7, (8)^8, + ...
* This is affordable to brute force, if we do until 10 characters, permutations = 1227096064

* IF it doesn't work in that range it's too much. 
* HOWEVER the tip says it won't take longer than a few seconds
* UPDATE: It became too much

Input 1: L1 + 5, L2 + 2, L3 + 1, L4 + 7, L5 + 5
Input 2: L1 + 13, L2 - 7, L3 - 4, L4 + 1, L5 + 5
Input 3: L1 + 9, L2 + 12, L3 + 9, L4 + 70, L5 - 4
Input 4: L1 - 11, L2 + 9, L3 + 0, L4 + 5, L5 - 13
Input 5: L1 + 4, L2 + 17, L3 + 12, L4 + 9, L5 + 24
Input 6: L1 + 11, L2 - 17, L3 + 21, L4 + 5, L5 + 14
Input 7: L1 + 15, L2 + 31, L3 + 22, L4 - 12, L5 + 3
Input 8: L1 + 19, L2 - 12, L3 + 4, L4 + 3, L5 - 7

* Going to use my permutation program from algorithm github (changed to number input)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void brute_forcer(int size, char *string);
void print_current(char *A);
int checkString(char *A);

int lock[5] = {300};

int main(int argc, char *argv[]) {
    
    char *string = "12345678";
    int starting_size = 13;
    char *new_string = malloc(sizeof(char) * starting_size + 1);
    
    strcpy(new_string, string);
    
    for (; starting_size < 14; starting_size++) {
        brute_forcer(starting_size, new_string);
    }
    
    printf("We can expect N permutations where N is (unique letters in the word)^size\n");

    return EXIT_SUCCESS;
}

void brute_forcer(int size, char *string) {

    int *element_pos = malloc(sizeof(int) * size);           // Position of each element in string.
    char *A = malloc(sizeof(char) * size + 1);                  // e.g [0,0,0,0,0] = [m,m,m,m,m]
    for (int i = 0; i < size; i++) {
        A[i] = string[0];
        element_pos[i] = 0;
    }
    
    char last_element = string[strlen(string) - 1];
    
    int current_position = 0;
    int current_element = size - 1;
    int count = 0;
    
    while (1) {
        A[current_element] = string[element_pos[current_element]];
        element_pos[current_element]++;
        if (checkString(A)) {
            printf("The combination was %s\n", A);
            break;
        }
        count++;
        if (A[current_element] == last_element) {
            int temp = current_element;
            while (A[temp] == last_element) {
                A[temp] = string[0];
                element_pos[temp] = 0;
                temp--;
                if (temp == -1) {
                    printf("Number of permutations = %d\n", count);
                    return;
                } 
            }
            element_pos[temp]++;
            A[temp] = string[element_pos[temp]];
            element_pos[current_element] = 0;
            A[current_element] = string[element_pos[current_element]];
            if (checkString(A)) {
                printf("The combination was %s\n", A);
                break;
            }
        }
    }
   free(A);
}

// Checks if it's the right combination

int checkString (char *A) {
    
    // Resetting
    for (int i = 0; i < 5; i++) {
        lock[i] = 300;
    }
    
    for (int i = 0; i < strlen(A); i++) {
        switch (A[i]) {
            case ('1'):
                lock[0] = lock[0] + 5;
                lock[1] = lock[1] + 2;
                lock[2] = lock[2] + 1;
                lock[3] = lock[3] + 7;
                lock[4] = lock[4] + 5;
                break;
            case ('2'):
                lock[0] = lock[0] + 13;
                lock[1] = lock[1] - 7;
                lock[2] = lock[2] - 4;
                lock[3] = lock[3] + 1;
                lock[4] = lock[4] + 5;  
                break;
            case ('3'):
                lock[0] = lock[0] + 9;
                lock[1] = lock[1] + 12;
                lock[2] = lock[2] + 9;
                lock[3] = lock[3] + 70;
                lock[4] = lock[4] - 4;  
                break;
            case ('4'):
                lock[0] = lock[0] - 11;
                lock[1] = lock[1] + 9;
                // lock[2] = lock[2] + 0;
                lock[3] = lock[3] + 5;
                lock[4] = lock[4] - 13;  
                break;
            case ('5'):
                lock[0] = lock[0] + 4;
                lock[1] = lock[1] + 17;
                lock[2] = lock[2] + 12;
                lock[3] = lock[3] + 9;
                lock[4] = lock[4] + 24;  
                break;
            case ('6'):
                lock[0] = lock[0] + 11;
                lock[1] = lock[1] - 17;
                lock[2] = lock[2] + 21;
                lock[3] = lock[3] + 5;
                lock[4] = lock[4] + 14;  
                break;
            case ('7'):
                lock[0] = lock[0] + 15;
                lock[1] = lock[1] + 31;
                lock[2] = lock[2] + 22;
                lock[3] = lock[3] - 12;
                lock[4] = lock[4] + 3;  
                break;
            case ('8'):
                lock[0] = lock[0] + 19;
                lock[1] = lock[1] - 12;
                lock[2] = lock[2] + 4;
                lock[3] = lock[3] + 3;
                lock[4] = lock[4] - 7;  
                break;
        }   
    }
    
    /*
    printf("Locks: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", lock[i]);
    }    
    printf("\n");
    */
    return (lock[0] == 400 && lock[1] == 400 && lock[2] == 400 && lock[3] == 400 && lock[4] == 400);
}

// Printing will slow it down a lot
void print_current(char *A) {

    for (int i = 0; i < strlen(A); i++) {
        printf("%c", A[i]);
    }
    printf("\n");
}








