from datetime import datetime
import sqlite3 
from tkinter import INSERT
conn = sqlite3.connect("Monopatines2.db")
conn.commit()
conn.close()

def creaTabla():
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Monopatines2(
        id_mono INTEGER PRIMARY KEY AUTOINCREMENT,
        marca VARCHAR(30),
        modelo VARCHAR(30),
        color VARCHAR(30),
        potencia VARCHAR(30),
        precio INTEGER,
        fechaUltimoPrecio DATETIME)""")
    conn.commit()
    conn.close()

def insertarTabla():
    marca=str(input("Ingrese marca: "))
    modelo=str(input("Ingrese Modelo: "))
    color=str(input("Ingrese Color : "))
    precio=input("Ingrese precio: ")
    potencia = input("Ingrese la potencia de su monopatin :" + "W ")
    fechaUltimoPrecio = datetime.now()
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Monopatines2 VALUES(NULL ,'{marca}', '{modelo}', '{color}', {potencia}, {precio}, {fechaUltimoPrecio.hour})")
    conn.commit()
    conn.close()

def precioAumento():
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    historicoprecios = f"SELECT * FROM Monopatines2"
    cursor.execute(historicoprecios)
    dat = cursor.fetchall()
    conn.commit()
    conn.close()
    print(dat)

def leerTabla():
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Monopatines2"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def cambiarPrecio():
    buscar_por_id = input('ID del monopatin: ')
    nuevoPrecio = input('Nuevo precio: ')
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    instruccion = f"UPDATE Monopatines2 SET precio={nuevoPrecio} WHERE id={buscar_por_id}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def borrarMonopatin():
    borrarId = input("Ingrese ID del monopatín a borrar: ")
    conn = sqlite3.connect('Monopatines2.db')
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Monopatines2 WHERE id={borrarId}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

i=0
while i == 0:
    print("menu")
    print("1-Ingresar monopatin/es: ")
    print("2-Ver monopatin/es: ")
    print("3-Modificar precio: ")
    print("4-Borrar monopatin/es")
    print("5-Salir")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese monopatin/es:")
        insertarTabla()
    elif opcion == 2:
        leerTabla()
    elif opcion == 3:
        cambiarPrecio()
    elif opcion == 4:
        borrarMonopatin()
    elif opcion == 5:
        precioAumento()
    elif opcion == 6:
        print("Gracias por usar nuestro sistema")
        break
        

    