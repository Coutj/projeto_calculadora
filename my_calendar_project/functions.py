from datetime import date
import calendar
import constants

def getMonth():
    
    actualMonth = date.today().strftime('%m')
    return  constants.MONTHS [int(actualMonth) - 1]
    

def printCalendar():
    
    endOfCalLine = 1
    year = int(date.today().strftime('%Y'))
    month = int(date.today().strftime('%m'))
    
    numberOfDays = calendar.monthrange(year, month)[1]

    for index in range (1, numberOfDays + 1): 
    
        if (index == int(date.today().strftime("%d"))):
            print (constants.PRINT_WITH_COLOR, end="")
        if ( endOfCalLine <= 6):
            print ("{: >2}".format(index), end=" ")
            print (constants.PRINT_WITHOUT_COLOR + "{: >0}".format(""), end="")
            endOfCalLine += 1;
        else:
            print ("{: >2}".format(index))
            print (constants.PRINT_WITHOUT_COLOR + "{: >4}".format("") )
            endOfCalLine = 1;
