from datetime import date
import calendar

import constants
from functions import getMonth

monthText = getMonth();
year = date.today().strftime('%Y')

numberOfDays = calendar.monthrange(int(date.today().strftime('%Y')), int(date.today().strftime('%m')))[1]

print ("{: >24}".format(monthText +" " + year))
print ()

endOfLine = 1
for index in range (1, numberOfDays + 1): 
    
    if (index == int(date.today().strftime("%d"))):
        print (constants.PRINT_WITH_COLOR, end="")
    if ( endOfLine <= 6):
        print ("{: >4}".format(index), end=" ")
        print (constants.PRINT_WITHOUT_COLOR + "{: >0}".format(""), end="")
        endOfLine += 1;
    else:
        print ("{: >4}".format(index))
        print (constants.PRINT_WITHOUT_COLOR + "{: >4}".format("") )
        endOfLine = 1;
        
print ("\n")
print ("{: >10}".format( constants.WEEKDAYS [date.today().weekday()] ))
print()
    


