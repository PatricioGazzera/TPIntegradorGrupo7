import sqlite3
from tkinter import INSERT

def creaTabla():
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE MONOPATINES(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca VARCHAR(30) UNIQUE,
        precio FLOAT NOR NULL,
        cantidad INTEGER,
        disponible INTEGER)""")
    conn.commit()
    conn.close()

def insertarTabla():
    id=input("Ingrese id: ")
    marca=str(input("Ingrese marca: "))
    precio=input("Ingrese precio: ")
    cantidad=input("Ingrese cantidad: ")
    disponible=input("Ingrese cantidad disponible: ")
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MONOPATINES VALUES({id}, '{marca}', {precio}, {cantidad}, {disponible})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def leerTabla():
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM MONOPATINES"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def cambiarPrecio():
    buscar_por_id = input('ID del monopatin: ')
    nuevoPrecio = input('Nuevo precio: ')
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()

