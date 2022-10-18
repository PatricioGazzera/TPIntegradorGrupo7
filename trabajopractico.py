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
    id=input("ingrese id: ")
    marca=str(input("ingrese marca: "))
    precio=input("ingrese precio: ")
    cantidad=input("ingrese cantidad: ")
    disponible=input("ingrese cantidad disponible: ")
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO MONOPATINES VALUES({id}, '{marca}', {precio}, {cantidad}, {disponible})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()