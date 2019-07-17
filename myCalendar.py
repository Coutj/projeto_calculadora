from datetime import date
import calendar

months = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", 
          "Setembro", "Outubro", "Novembro", "Dezembro"]
weekDay = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def getMonth():
    
    actualMonth = date.today().strftime('%m')
    return months [int(actualMonth) - 1]
        
        

monthText = getMonth();
year = date.today().strftime('%Y')

numberOfDays = calendar.monthrange(int(date.today().strftime('%Y')), int(date.today().strftime('%m')))[1]

print ("{: >24}".format(monthText +" " + year))
print ()

endOfLine = 1
for index in range (1, numberOfDays + 1):
    
    if (index == int(date.today().strftime("%d"))):
        print ('\033[95m', end="")
    if ( endOfLine <= 6):
        print ("{: >4}".format(index), end=" ")
        print ('\033[0m' + "{: >0}".format(""), end="")
        endOfLine += 1;
    else:
        print ("{: >4}".format(index))
        print ('\033[0m' + "{: >4}".format("") )
        endOfLine = 1;
        
print ("\n")
print ("{: >10}".format(weekDay[date.today().weekday()]))
print()
    


