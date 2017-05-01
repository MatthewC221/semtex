#!/usr/bin/python

import sys

before = ""
after = ""

"""
I don't actually know the encryption method, but by copying the data, the increments are the same.
Therefore I read from a data file with an example, and read it backwards so I could copy the same steps.

Mistakes: I used the data AAAAAAAAAAAA, the A's could've been in the wrong positions but I wouldn't have known,
this is why my initial creation was wrong. Refer to the permutation array

"""
if (len(sys.argv) != 2):
    print "Usage ./level1.py <13 length string>"

else:
    starting_string = sys.argv[1]
    if (len(starting_string) != 13):
        exit()
        
    list_string = list(starting_string)

    flag = False
    print list_string
    for line in reversed(open("level1_data.txt", "r").readlines()):
        line = line.strip()
        if (flag):
            after = line
            for i in range(0, len(after)):
                difference = ord(before[i]) - ord(after[i])
                if (ord(list_string[i]) - difference > 90):                
                    list_string[i] = chr(ord(list_string[i]) - difference - 26)
                elif (ord(list_string[i]) - difference < 65):
                    list_string[i] = chr(ord(list_string[i]) - difference + 26)
                else:
                    list_string[i] = chr(ord(list_string[i]) - difference)    
            before = after
            print list_string 
            print ""    
        else:
            flag = True
            before = line
    
    # Final position change, (I analysed this part by hand)
    permutation = [10, 7, 12, 9, 2, 11, 4, 1, 6, 3, 8, 5, 0] 
    for i in range(0, len(list_string)):
        sys.stdout.write(list_string[permutation[i]])

    print ""
