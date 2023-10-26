#Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Por ejemplo: *(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+ Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: *(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+
def origen_list(list):
  city=input("Ingrese su ciudad natal: ").lower
  country=input("Ingrese su pais: ").lower
  list.append((city,country))
  return list

##Funcion para añadir pasajeros
def add_traveler(T_list,H_list):
  while True:
    name=input("Ingrese el nombre del pasajero: ").lower()
    dni=int(input("Ingrese el DNI del pasajero: "))
    destination=input("Ingrese el destino del pasajero: ").lower()
    T_list.append((name,dni,destination))
    #print("De que ciudad es el pasajero?")
    origen_list(H_list)
    choice=input("¿Desea ingresar otro pasajero? (s/n): ")
    if choice=='n':
      break


#funcion para buscar pasajeros por dni
def search_traveler(list,ID):
  for i in list:
    if i[1]==ID:
      return i[2]
  return None


#funcion para buscar ciudades/paises
def search_city(list,city,n):
  cont=0
  for i in list:
    if i[n]==city:
      cont+=1
  return cont
