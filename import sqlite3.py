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
    id=input("ingrese precio: ")
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
    instruccion = f"UPDATE MONOPATINES SET precio={nuevoPrecio} WHERE id={buscar_por_id}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def borrarMonopatin():
    borrarId = input("Ingrese ID del monopatín a borrar: ")
    conn = sqlite3.connect('MONOPATINES.db')
    cursor = conn.cursor()
    instruccion = f"DELETE FROM MONOPATINES WHERE id={borrarId}"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

i=0
while i == 0:
    print("        Menu")
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