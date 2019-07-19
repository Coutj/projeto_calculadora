from datetime import date
import constants

def getMonth():
    
    actualMonth = date.today().strftime('%m')
    return  constants.MONTHS [int(actualMonth) - 1]
