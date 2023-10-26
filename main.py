from fun import*
print("Bienvenido al sistema de registro de pasajeros")
travelers=[("Camila",1234567,"san juan"),("Juan",3435363,"san juan"),("Maria",343434,"cordoba")]#
hometown=[("santiago","chile"),("buenos aires","argentina"),("mendoza","argentina")]#list()

#como el ejercicio pide que ingrese un solo destino, asumi que seria la ciudad y no el pais, si no deberia agregar un argumento mas de destino (nombre,dni,ciudad destino,pais destino); mientras que la lista de tuplas de ciudades de origen si tiene (ciudad origen,pais origen)
#por lo tanto para la opcion de "ver cuantos pasajeros viajan a ese pais", podria cambiarla a "cuantos pasajeros son de ese pais" o agregar el argumento a la tupla de la lista "travelers" del pais para viajar, pero el programa no sabe si una ciudad X es de ese pais y deberia validar eso; asi que decidi modificar el menu
while True:
  print("Seleccione una opcion:")
  print("1. Agregar pasajeros a la lista de viajeros")
  print("2. Ver a qué ciudad viaja (Ingrese DNI del pasajero))")
  print("3. Ver cuantos pasajeros viajan a una ciudad (Ingrese nombre de la ciudad)")
  print("4. Ver cuantos pasajeros son de origen de un pais (Ingrese pais)")
  print("5. Salir del programa")
  choice=int(input("Ingrese una opcion: "))
  print("")
  if choice==1:
    print("Agregar viajeros")
    add_traveler(travelers,hometown)
    print("")
  elif choice==2:
    print("Ver a que ciudad viaja")
    dni=int(input("Ingrese el DNI del pasajero: "))
    dest=search_traveler(travelers,dni)
    print(f"El pasajero {dni} buscado viaja a {dest}")
    print("")
  elif choice==3:
    print("Ver cuantos pasajeros viajan a una ciudad")
    city=input("Ingrese la ciudad: ").lower()
    
    total=search_city(travelers,city,2)#el 2 nos va a dar la ciudad destino
    print(f"Hay {total} pasajeros que viajan a {city}")
    print("")
  elif choice==4:
    print("Ver cuantos pasajeros son de origen de un pais")
    country=input("Ingrese el pais: ").lower()
    total=search_city(hometown,country,1)#el 1 nos va a dar el pais origen
    print(f"Hay {total} pasajero/s que son natales de {country}")
    print("")
  elif choice==5:
    print("Gracias por usar el programa")
    break
  else:
    print("Opcion incorrecta")
  