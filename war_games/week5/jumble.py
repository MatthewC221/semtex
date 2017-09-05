#!/usr/bin/python

import sys

# VAARIM_ZCZEWZRRHEROD_VHE__VVQQDZAGWKZIKG_DBKESWASSBCKQB_S_VZOAEVNZZDDCQ___QDVAVT_AA_OZEQQVBMQ

def jumble_back(temp):      # temporary string
    
    new = []
    for i in range(0, len(temp)):
        if (temp[i] == 'A'):  
            new.append('R')
        elif (temp[i] == 'B'):  
            new.append('W')
        elif (temp[i] == 'C'):  
            new.append('D')
        elif (temp[i] == 'E'):  
            new.append('Z')
        elif (temp[i] == 'F'):  
            new.append('G')
        elif (temp[i] == 'G'):  
            new.append('O')
        elif (temp[i] == 'H'):  
            new.append('C')
        elif (temp[i] == 'I'):  
            new.append('S')
        elif (temp[i] == 'J'):  
            new.append('U')
        elif (temp[i] == 'K'):  
            new.append('H')
        elif (temp[i] == 'L'):  
            new.append('T')
        elif (temp[i] == 'M'):  
            new.append('N')
        elif (temp[i] == 'N'):  
            new.append('B')
        elif (temp[i] == 'O'):  
            new.append('A')
        elif (temp[i] == 'P'):  
            new.append('I')
        elif (temp[i] == 'Q'):  
            new.append('L')
        elif (temp[i] == 'R'):  
            new.append('V')
        elif (temp[i] == 'S'):  
            new.append('K')
        elif (temp[i] == 'T'):  
            new.append('Q')
        elif (temp[i] == 'U'):  
            new.append('E')
        elif (temp[i] == 'V'):  
            new.append('X')
        elif (temp[i] == 'W'):  
            new.append('P')
        elif (temp[i] == 'X'):  
            new.append('F')
        elif (temp[i] == 'Y'):  
            new.append('M')
        elif (temp[i] == 'Z'):  
            new.append('Y')
        elif (temp[i] == '_'):
            new.append(' ')
    return new
    
original = jumble_back("VAARIM_ZCZEWZRRHEROD_VHE__VVQQDZAGWKZIKG_DBKESWASSBCKQB_S_VZOAEVNZZDDCQ___QDVAVT_AA_OZEQQVBMQ")
for i in range(0, len(original)):
    sys.stdout.write(original[i])
    
print ""




