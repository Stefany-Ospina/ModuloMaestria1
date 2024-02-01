import random
import sqlite3

def generar_censo(cantidad):
  censo=[]
  alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numero=0

  for _i in range(cantidad):
      aumento =random.randint(1,2)
      numero += aumento

      letras = random.sample(alfabeto,5)
      nombre = "".join(letras)#unir las letras aleatorias

      edad = random.randint(18,99)

      impuestos = random.choice((True, True, True, False))

      censo.append([numero, nombre, edad, impuestos])
  return censo

def main():
  cantidad_registros=1050000
  censo=generar_censo(cantidad_registros)
#conexion a la base de datos
  conn=sqlite3.connect("censo.db")#sino tiene la base de datos la crea
  c=conn.cursor()#se crea cursor para ejecutar las sentencias sql
#crear una tabla sino existe
  c.execute('''
          CREATE TABLE IF NOT EXISTS censo(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          numero INTEGER,
          nombres TEXT,
          edad INTEGER,
          impuestos BOOLEAN)
          ''')
  c.executemany('INSERT INTO censo (numero,nombre, edad, impuestos) VALUES(?,?,?,?)', censo)
  conn.commit()
  conn.close()
  