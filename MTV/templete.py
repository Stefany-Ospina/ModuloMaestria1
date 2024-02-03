from model import obtener_libros


def renderizar_template(libros):
  html="<h1>lista de libros</h1>"
  for libro in libros:
    html+=f"<p>ID: {libro['id']} ,<br> Titulo: {libro['titulo']}, <br>Autor: {libro['autor']}</p>"
  return html
#integrar la vista y el template

def mostrar_libros_con_template():
  libros=obtener_libros()
  html=renderizar_template(libros)
  print(html)

mostrar_libros_con_template()