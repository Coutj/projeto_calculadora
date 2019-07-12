from datetime import date

months = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", 
          "Setembro", "Outubro", "Novembro", "Dezembro"]

def GetMMYYYY (tipo):
    
    tipo = tipo.upper()
    
    if (tipo.upper() == "MM"):
        actualMonth = date.today().strftime('%m')
        print (months [int(actualMonth)])
    else:
        print("Errou")



print (type(date.today()))
GetMMYYYY("mm");

