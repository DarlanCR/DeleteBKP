from datetime import datetime
import os


path = 'C:/Chef/Backups/'


mesAt = int(datetime.today().strftime('%m'))
ano = int(datetime.today().strftime('%y'))
# # os.chdir(path)
# # dir = os.getcwd()
i = 0
mes = mesAt - 3

def data():
    if mesAt <= 3:
        old = "_1"+str(mes)+"_20"+str(ano-1)+"_"
    else:
        old = "_0"+str(mes)+"_20"+str(ano)+"_"
    return old

try:
    while i < 3:
        for file in os.listdir(path):
            if file.startswith(('mydata','chef')):
                # print(file)
                if data() in file:
                    try:
                        os.remove(path+file)
                    except:
                        print("Não excluiu")
                    else:
                        print("Excluiu")
        mes = mes - 1
        
        if mes == 0:
            break 
except:
    print("Deu ruim")

else:
    print("Finalizado")