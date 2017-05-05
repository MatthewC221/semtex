#!/usr/bin/python

import sys
import itertools

"""
Input 1: L1 + 5, L2 + 2, L3 + 1, L4 + 7, L5 + 5
Input 2: L1 + 13, L2 - 7, L3 - 4, L4 + 1, L5 + 5
Input 3: L1 + 9, L2 + 12, L3 + 9, L4 + 70, L5 - 4
Input 4: L1 - 11, L2 + 9, L3 + 0, L4 + 5, L5 - 13
Input 5: L1 + 4, L2 + 17, L3 + 12, L4 + 9, L5 + 24
Input 6: L1 + 11, L2 - 17, L3 + 21, L4 + 5, L5 + 14
Input 7: L1 + 15, L2 + 31, L3 + 22, L4 - 12, L5 + 3
Input 8: L1 + 19, L2 - 12, L3 + 4, L4 + 3, L5 - 7
"""
locks = [300, 300, 300, 300, 300]

input1 = [5, 2, 1, 7, 5]
input2 = [13, -7, -4, 1, 5]
input3 = [9, 12, 9, 70, -4]
input4 = [-11, 9, 0, 5, -13]
input5 = [4, 17, 12, 9, 24]
input6 = [11, -17, 21, 5, 14]
input7 = [15, 31, 22, -12, 3]
input8 = [19, -12, 4, 3, -7]

all_inputs = [input1, input2, input3, input4, input5, input6, input7, input8]

def check_combinations(combinations):

    for i in range(0, len(combinations)):
        j = int(combinations[i])
        locks[0] = locks[0] + all_inputs[j][0]
        locks[1] = locks[1] + all_inputs[j][1]
        locks[2] = locks[2] + all_inputs[j][2]
        locks[3] = locks[3] + all_inputs[j][3]
        locks[4] = locks[4] + all_inputs[j][4]


    return (locks[0] == 400 and locks[1] == 400 and locks[2] == 400
     and locks[3] == 400 and locks[4] == 400)

def clear_locks():

    for i in range(0, 5):
        locks[i] = 300

# Length starts as 5 because it is minimum 5 permutations for lock1 to reach goal

length = 5         
while (1):
    for combinations in itertools.combinations_with_replacement(range(0, 8), length):
        if (check_combinations(combinations)):
            print "Combination = " + str(combinations)
            sys.exit()
        clear_locks()
    length += 1
 
 




   
    
    
