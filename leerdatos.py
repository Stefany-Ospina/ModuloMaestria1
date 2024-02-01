import sqlite3
def lee_datos():
  conn = sqlite3.connect("censo.db")
  cursor=conn.cursor()
  