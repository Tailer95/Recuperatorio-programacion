import csv

inventario = "C:\\Users\\Usuario\\Desktop\\Recuperatorio Programacion\\inventario.csv"

def leer_archivo():
    "Lee un archivo CSV y retorna una lista con sus datos"
    with open(inventario, mode="r") as archivo:
        datos = archivo.readlines()
        for i in range(len(datos)): 
            datos[i] = datos[i].replace("\n", "").split(",")
    return datos





def buscar_producto(datos)->str:
    "Busca un producto en la lista de inventario, si se encuentra retorna el producto con sus respectivos detalles"
    encontrado = False
    producto = input("Ingresar un producto para buscar en el inventario: ").lower()
    for i in range(len(datos)): 
        if datos[i][0].lower() == producto: 
            retorno = f"Se ha encontrado {datos[i][0]}\nDetalles del producto:\nPrecio: {datos[i][1]}\nCantidad: {datos[i][2]}"
            encontrado = True
    if encontrado == False: 
        retorno = f"No se encontró el producto {producto}"
    return retorno

def ordenar_por_precio(datos): 
    "Ordena el inventario por precio de manera ascendente"
    ordenada = False
    while(ordenada == False): 
        ordenada = True
        for i in range(1, len(datos) - 1): 
            if float(datos[i][1]) > float(datos[i + 1][1]): 
                aux = datos[i]
                datos[i] = datos[i + 1]
                datos[i + 1] = aux
                ordenada = False
    return datos

def ordenar_por_cantidad(datos):
    "Ordena el inventario por cantidad de manera ascendente"
    ordenada = False
    while(ordenada == False): 
        ordenada = True
        for i in range(1, len(datos) - 1): 
            if int(datos[i][2]) > int(datos[i + 1][2]): 
                aux = datos[i]
                datos[i] = datos[i + 1]
                datos[i + 1] = aux
                ordenada = False
    return datos

def listar_inventario(datos):
    "Muestra por consola el nombre de los productos en el inventario"
    print("Producto")
    for i in range(1, len(datos)): 
        print(datos[i][0],datos[i][1],datos[i][2])

def actualizar_cantidad(datos:list):
    "Disminuye la cantidad disponible de un producto después de una venta"
    producto = input("Ingrese el producto vendido: ").lower()
    cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
    band = False
    for i in range(1, len(datos)): 
        if datos[i][0].lower() == producto: 
            stock = int(datos[i][2])
            if stock >= cantidad_vendida:
                datos[i][2] = str(stock - cantidad_vendida)
                print(f"La venta se realizó y el stock del {datos[i][0]} actual es de: {datos[i][2]}")
            else:
                print(f"No hay suficiente stock de {datos[i][0]}")
            band = True
            break
    if not band:
        print(f"El producto '{datos[i][0]}' no se encuentra en el inventario.")

def escribir_archivo(datos):
    "Guarda los datos actualizados en el inventario"
    with open(inventario, mode="w", newline="") as archivo:
        datos_nuevos = csv.writer(archivo)
        datos_nuevos.writerows(datos)
    print("Se guardo correctamente el archivo")

def mappear_precios(datos)->list:
    for i in range(1, len(datos)):
        datos[i][1] = float(datos[i][1]) * 1.1
    return datos


def menu():
    datos = leer_archivo()
    opcion = 0
    while opcion != 7:
        print ("1- Buscar Producto")
        print ("2- Ordenar inventario (por precio o cantidad)")
        print ("3- Listar inventario")
        print ("4- Actualizar cantidades")
        print ("5- Escribir un archivo")
        print ("6- Ingremetar un 10% todos los precios")
        print ("7- Salir del programa")
        opcion = int(input("Ingrese una opción del 1 al 7: "))
        if opcion == 1:
            print (buscar_producto(datos))
        elif opcion == 2:
            seleccion = input("Quiere ordenar por precio o cantidad (p/c): ").lower()
            if seleccion == "p":
                ordenar_por_precio(datos)
                print("Se ha ordenado correctamente por precio.")
            elif seleccion == "c":
                ordenar_por_cantidad(datos)
                print("Se ha ordenado correctamente por cantidad.")
            else:
                print("No es una opción valida")
        elif opcion == 3:
            listar_inventario(datos)
        elif opcion == 4:
            actualizar_cantidad(datos)
        elif opcion == 5:
            escribir_archivo(datos)
        elif opcion == 6:
            mappear_precios(datos)
        elif opcion == 7:
            print("Gracias por usar el programa")
            break

menu()