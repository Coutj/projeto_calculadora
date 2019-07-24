from datetime import date

import constants
from functions import getMonth, printCalendar

def main():
    
    monthText = getMonth();
    year = date.today().strftime('%Y')


    print();
    print ("{: >15}".format(monthText +" " + year))
    print ()
    printCalendar()
    print ("\n")
    print ("{: >11}".format( constants.WEEKDAYS [date.today().weekday()] ))
    print()
        

if (__name__ == "__main__"):
	main()
