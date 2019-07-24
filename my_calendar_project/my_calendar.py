from datetime import date

import constants
import functions

def main():
    
    monthText = functions.getMonth()
    year = date.today().strftime('%Y')


    print();
    print ("{: >15}".format(monthText +" " + year))
    print ()
    functions.printCalendar()
    print ("\n")
    print ("{: >11}".format( constants.WEEKDAYS [date.today().weekday()] ))
    print()
        

if (__name__ == "__main__"):
	main()
