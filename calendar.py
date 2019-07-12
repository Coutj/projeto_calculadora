from datetime import date
import calendar

months = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", 
          "Setembro", "Outubro", "Novembro", "Dezembro"]

def getMonth(tipo):
    
    tipo = tipo.upper()
    
    if (tipo == "MM"):
        
        actualMonth = date.today().strftime('%m')
        return months [int(actualMonth)]
        
        

monthText = getMonth("mm");
year = date.today().strftime('%Y')



print (calendar.monthrange(2019, 1)[1])  
print ( monthText + " " + year)

