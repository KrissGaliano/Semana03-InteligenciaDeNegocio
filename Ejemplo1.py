import pymysql
from sqlalchemy import create_engine
import pandas as pd
cnx=create_engine('mysql+pymysql://root:@localhost:3306/sakila').connect()
sql= 'select * from payment'
data=pd.read_sql(sql,cnx)
lista=pd.DataFrame(data)
print("------------------------EJERCICIO 1------------------------")
print("")
print(lista)

#print('Registros: ', len(lista.index))
#print('Campos: ', len(lista.count()))
#print('Media: ', lista['amount'].mean())
#print('Moda: ', lista['amount'].mode())

#-----------------------------------------------------------------------------------------------------------------------------

def Ejercicio2():
    fpx = "select * from customer"
    datos = pd.read_sql(fpx, cnx)

    print("-----------------EJERCICIO2--------------------")
    print("")
    print("Datos de medida central - CUSTOMER")
    print("")
    print(datos.describe())
    print("")

def Ejercicio3():
    fpx = "select * from payment"
    datos = pd.read_sql(fpx, cnx)
    print("--------------EJERCICIO 3-----------------------")
    print("")
    print("Datos de medida central - 'PAYMENT'")
    print("")
    print("Media: ", datos['amount'].mean())
    print("Mediana: ", datos['amount'].median())
    print("Moda: ", datos['amount'].mode())
    print("")

def Ejercicio4():
    fpx = "select * from film"
    datos = pd.read_sql(fpx, cnx)
    print("------------------EJERCICIO 4-------------------")
    print("")
    print("Datos de medida central - 'REPLACEMENT COST'")
    print("")
    print("Media: ", datos['replacement_cost'].mean())
    print("Mediana: ", datos['replacement_cost'].median())
    print("Moda: ", datos['replacement_cost'].mode())
    print("")

def Ejercicio5():
    fpx = "select amount from payment"
    datos = pd.read_sql(fpx, cnx)
    print("----------------EJERICIO 5---------------------")
    print("")
    print("Datos de medida central - AMOUNT / PAYMENT")
    print("")
    print("Media: ", datos['amount'].mean())
    print("Mediana: ", datos['amount'].median())
    print("Moda: ", datos['amount'].mode())
    print("")


#Ejercicio 2
Ejercicio2()

#Ejercicio 3
Ejercicio3()

#Ejercicio 4
Ejercicio4()

#Ejercicio 5
Ejercicio5()