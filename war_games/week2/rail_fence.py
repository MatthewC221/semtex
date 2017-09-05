#!/usr/bin/python

import sys

# Incomplete rail_fence

temp_string = 'S_   ltes e__owesft4ya\'h r_ernadinhohn_hstfeamion coo iost  lhrooidskeutsio t,aPeeut_eemlc tmkhegi_wschoool31neOen Cbale4h s tee_  oi_r yjnsr  iat_.>dslu}4 nd asthsnCg-  it_ Misdirection_tCaeesa Oe1elr__firiOR_lelsmk_hlabsfkabM{fbbliuec_p  eiecn P1oaubco a_ite_headm34rebihchtHo4c'

divider = 12

while (divider < 20):
    counter = 0
    starting_index = 188
    while (counter < 250):
        print temp_string[starting_index],
        print "." * divider,
        starting_index = starting_index + 1
        
        if (starting_index > 279):
            starting_index = starting_index - 279
        counter += 1
        if (counter % 5 == 0 and counter != 0):
            print ""
    print "\n\n\n\n"
    divider += 1










