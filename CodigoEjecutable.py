from CodigoAlbum import mostrar_menu,agregar_album,buscar_por_anio,buscar_por_genero,eliminar_album,mostrar_todos
while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            agregar_album()
        elif opcion == 2:
            buscar_por_anio()
        elif opcion == 3:
            buscar_por_genero()
        elif opcion == 4:
            eliminar_album()
        elif opcion == 5:
            mostrar_todos()
        elif opcion == 6:
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
    except ValueError:
        print("Por favor ingrese un número válido.")