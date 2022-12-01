import requests
import json


url = 'http://127.0.0.1:8000/api/products'

def showProducts():
	peticion = requests.get(url)
	productos = json.loads(peticion.content)
	# print(productos)

	# Podemos mostrar este formato de json en una tabla

	# Ahora lo vamos a mostra un formato de tabla
	print("{:<3} {:<50} {:<100} {:<10}".format('#','PRODUCTO', 'DESCRIPCION', 'PRECIO'))
	# Creamos un ciclo o un bucle for
	num = 0
	for producto in productos:
		num = num+1
		print("{:<3} {:<50} {:<100} {:<10}".format(str(num)
			,producto['name'],producto['description'],producto['price']))


# Podemos crear una funcion para poder guardar

def guardar(nombre, descripcion, precio):
	paramentros = {'name':nombre,'description':descripcion,'price':precio}
	peticion = requests.post(url,paramentros)
	respuesta = json.loads(peticion.content)

	status = respuesta[0]['status']
	if status == 'error':
		claves = [] # Esto va hacer un array vacio
		errores = respuesta[1]['errors']
		for err in errores:
			claves.append(err) #Por cada error que 
			#hecista vamos a ir  guardado sus claves
		for c in claves:
			print(errores[c][0])
		else:
			print('Producto guardado')

	# Yo puedo guadar un producto de aqui mismo
	# guardar('loptop', 'muy veloz y grande', '40000')


# showProducts()
guardar('loptop','muy veloz y grande','50999')