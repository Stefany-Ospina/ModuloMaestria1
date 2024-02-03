from model import obtener_libros
def mostrar_libros():
  libros=obtener_libros()
  for libro in libros:
    print(f"ID:{libro['id']},título:{libro['titulo']},autor:{libro['autor']}")