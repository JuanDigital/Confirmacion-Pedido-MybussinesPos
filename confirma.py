import pyodbc
import pandas as pd
import numpy as np
import shutil
# Some other example server values are
#server = 'localhost' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'DEVELOPMENT\SQLEXPRESS' 
database = 'C:\MyBusinessDatabase\MyBusinessPOS2011.mdf' 
username = 'sa' 
password = '12345678'
'''
cantidad
unidad =kg
producto
costo
'''
lSubT=[]
lCodigo=[]


try:
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    print('conexion exitosa')

except:
    print('no conecto')

'''
cursor.execute("select cantidad,observ,precio from pedpar where pedido='1'") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


codsql="select cantidad,observ,precio from pedpar where pedido='1'"
consulta=pd.read_sql_query(codsql, cnxn)
consulta.head()
'''
entrada=input("ingresa el numero de pedido que quieras ver: ")
query = "select cantidad,observ,precio from pedpar where pedido="+entrada
pedido = pd.read_sql(query, cnxn)
##print(pedido.cantidad)
##print(pedido.precio)

shutil.copy("basic_template.html", "template.html")


for i in range(0,len(pedido)):
    nCant=float(pedido.iloc[i,0])
    nPre= float(pedido.iloc[i,2])
    subT=nCant*nPre
    #print (type(pedido.iloc[i,0]))
    #print(subT)
    lSubT.append(subT)
##    print(lSubT)
dfSubT=pd.DataFrame(lSubT)
##print(dfSubT)


#agregar subtotal a pedido
tFull=pedido.join(dfSubT)


tFull.to_html('tabla.html',header=False,index=False)

tabla=open('tabla.html','rt',encoding='utf-8')

codigo=tabla.readlines()

for j in codigo:
    #print(type(j))
    if len(j)!=37:
        if len(j)!=10:            
            print(j)
            lCodigo.append(j)
        else:
            j='</tr>'
            print(j)
            lCodigo.append(j)

tabla.close()



template=open('template.html','a',encoding='utf-8')

template.writelines(lCodigo)
template.close()




