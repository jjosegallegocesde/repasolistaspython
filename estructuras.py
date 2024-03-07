#Se declaran diccionarios = objetos
clienteUno={
    "id":5,
    "nombre":"edif1",
    "consumo":200
}

clienteDos={
    "id":58,
    "nombre":"edif2",
    "consumo":500
}

#se declara una lista = arreglo
clientesAsociados=[
    clienteUno,
    clienteDos
]


#Y AHORA QUE HAGO CON ESA LISTA?
#MI OBJETIVO SERA OBTENER LA INFORMACION DE LA LISTA
#RECORRER UNA LISTA O ARREGLO
#print(clientesAsociados)

'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''

#Programemos un foreach que es un for
#especializado en recorrer arreglos (listas)
for cliente in clientesAsociados:
    print(cliente["id"],'=>',cliente['consumo'],'KWH')
    print(f"{cliente["id"]}=>{cliente["consumo"]} KWH")