registro = {"123456789": "Persona 1" ,
            "987654321": "Persona 2",
            "454545454" : "Persona 3"}

productos = ["Hamburgesa", "Sanduche", "Gaseosa", "Papas"]
nombre=[]

input("Bienvenido, pulse sobre la pantalla para continuar ")
cedula = input("Digite su cédula:  ")

if cedula in registro:
    print("existe en el registro")
    nombre = registro[cedula]

else:
    nombre = input("No existe en el registro, digite su nombre:  ")
    registro[cedula] = nombre

lista = []

while True:
    for n,producto in enumerate(productos):
        print("{}.{}".format(n,producto))
    produc_selec = int(input("Digite número producto: "))
    lista.append(productos[produc_selec])
    consulta = (input("Desea finalizar (SI/NO): "))
    if consulta == "SI":
        break

pedido = "Datos del pedido: \n Cedula {}  \n Nombre {}  \n Pedido {}".format(cedula,nombre,lista)

print(pedido)





    


