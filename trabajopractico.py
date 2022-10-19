import sqlite3 
from tkinter import INSERT
conn = sqlite3.connect("Monopatines.db")
conn.commit()
conn.close()

def creaTabla():
    conn = sqlite3.connect('Monopatines.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE Monopatines(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca VARCHAR(30) UNIQUE,
        precio FLOAT NOR NULL,
        cantidad INTEGER,
        disponible INTEGER)""")
    conn.commit()
    conn.close()

def insertarTabla():

    marca = str(input("ingrese marca: "))
    precio = input("ingrese precio: ")
    cantidad = input("ingrese cantidad: ")
    disponible = input("ingrese cantidad disponible: ")
    conn = sqlite3.connect('MONOPATINES.db')

    id=input("ingrese id: ")
    marca=str(input("ingrese marca: "))
    precio=input("ingrese precio: ")
    cantidad=input("ingrese cantidad: ")
    disponible=input("ingrese cantidad disponible: ")
    conn = sqlite3.connect('Monopatines.db')

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO Monopatines VALUES({id}, '{marca}', {precio}, {cantidad}, {disponible})")
    conn.commit()
    conn.close()

def leerTabla():
    conn = sqlite3.connect('Monopatines.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM Monopatines"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def cambiarPrecio():
    buscar_por_id = input('ID del monopatin: ')
    nuevoPrecio = input('Nuevo precio: ')
    conn = sqlite3.connect('Monopatines.db')
    cursor = conn.cursor()
    instruccion = f"UPDATE Monopatines SET precio={nuevoPrecio} WHERE id={buscar_por_id}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def borrarMonopatin():

    borrarId = input("Ingrese ID del monopatin a borrar: ")
    conn = sqlite3.connect('MONOPATINES.db')
    borrarId = input("Ingrese ID del monopatín a borrar: ")
    conn = sqlite3.connect('Monopatines.db')
    cursor = conn.cursor()
    instruccion = f"DELETE FROM Monopatines WHERE id={borrarId}"
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