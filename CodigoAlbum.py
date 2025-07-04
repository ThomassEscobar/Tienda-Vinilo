albumes = [
    {'id': 'ALB001', 'titulo': 'A Night at the Opera', 'artista': 'Queen', 'genero': 'rock', 'anio': '1975', 'formato': 'vinilo', 'stock_vinilo': 10, 'stock_cd': 5, 'stock_digital': 3},
    {'id': 'ALB002', 'titulo': 'Thriller', 'artista': 'Michael Jackson', 'genero': 'pop', 'anio': '1982', 'formato': 'cd', 'stock_vinilo': 4, 'stock_cd': 12, 'stock_digital': 6},
    {'id': 'ALB003', 'titulo': 'Dark Side of the Moon', 'artista': 'Pink Floyd', 'genero': 'rock', 'anio': '1973', 'formato': 'vinilo', 'stock_vinilo': 8, 'stock_cd': 7, 'stock_digital': 5},
    {'id': 'ALB004', 'titulo': '21', 'artista': 'Adele', 'genero': 'pop', 'anio': '2011', 'formato': 'digital', 'stock_vinilo': 0, 'stock_cd': 2, 'stock_digital': 10},
    {'id': 'ALB005', 'titulo': 'Abbey Road', 'artista': 'The Beatles', 'genero': 'rock', 'anio': '1969', 'formato': 'vinilo', 'stock_vinilo': 9, 'stock_cd': 6, 'stock_digital': 2},
    {'id': 'ALB006', 'titulo': 'Back in Black', 'artista': 'AC/DC', 'genero': 'rock', 'anio': '1980', 'formato': 'cd', 'stock_vinilo': 3, 'stock_cd': 8, 'stock_digital': 5},
    {'id': 'ALB007', 'titulo': 'The Wall', 'artista': 'Pink Floyd', 'genero': 'rock', 'anio': '1979', 'formato': 'cd', 'stock_vinilo': 2, 'stock_cd': 9, 'stock_digital': 4},
    {'id': 'ALB008', 'titulo': 'Lemonade', 'artista': 'Beyoncé', 'genero': 'r&b', 'anio': '2016', 'formato': 'digital', 'stock_vinilo': 0, 'stock_cd': 1, 'stock_digital': 8}
]

generos_permitidos = [
    "rock", "pop", "jazz", "reggaetón", "clásica", "electrónica",
    "hip hop", "metal", "indie", "blues", "folk", "salsa", "cumbia", "r&b"
]

def mostrar_menu():
    print("\n*** MENÚ PRINCIPAL - TIENDA DE VINILOS ***")
    print("1. Agregar Álbum")
    print("2. Buscar Álbum por Año de Lanzamiento")
    print("3. Buscar Álbum por Género")
    print("4. Eliminar Álbum por ID")
    print("5. Mostrar Todos los Álbumes")
    print("6. Salir")

def validar_texto(campo, solo_letras=False):
    while True:
        valor = input(f"Ingrese {campo}: ").strip()
        if valor == "":
            print(f"{campo} no puede estar vacío.")
        elif solo_letras and not valor.replace(" ", "").isalpha():
            print(f"{campo} debe contener solo letras.")
        else:
            return valor

def validar_genero():
    print("\nGéneros permitidos:")
    for g in generos_permitidos:
        print(f"- {g.capitalize()}")
    while True:
        genero = input("Ingrese género musical: ").strip().lower()
        if genero in generos_permitidos:
            return genero
        else:
            print("Género no válido. Intente de nuevo.")

def validar_entero(campo):
    while True:
        try:
            valor = int(input(f"Ingrese {campo}: "))
            if valor < 0:
                print(f"{campo} no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Debe ingresar un número válido.")

def agregar_album():
    album = {}
    while True:
        id_album = validar_texto("ID del álbum (Ej: ALB009)").upper()
        if any(a["id"] == id_album for a in albumes):
            print("Ese ID ya está en uso. Intente con otro.")
        else:
            album["id"] = id_album
            break

    album["titulo"] = validar_texto("título del álbum")
    album["artista"] = validar_texto("artista")
    album["genero"] = validar_genero()
    album["anio"] = validar_texto("año de lanzamiento")
    album["formato"] = validar_texto("formato (vinilo, cd o digital)").lower()

    
    album["stock_vinilo"] = validar_entero("stock en vinilo")
    album["stock_cd"] = validar_entero("stock en CD")
    album["stock_digital"] = validar_entero("stock en formato digital")

    albumes.append(album)
    print("Álbum agregado exitosamente.")

def buscar_por_anio():
    anio = validar_texto("el año de lanzamiento a buscar")
    encontrados = [a for a in albumes if a["anio"] == anio]
    if encontrados:
        for album in encontrados:
            mostrar_album(album)
    else:
        print("No se encontraron álbumes para ese año.")

def buscar_por_genero():
    genero = validar_genero()
    encontrados = [a for a in albumes if a["genero"] == genero]
    if encontrados:
        for album in encontrados:
            mostrar_album(album)
    else:
        print("No se encontraron álbumes de ese género.")

def eliminar_album():
    id_album = validar_texto("el ID del álbum a eliminar").upper()
    for i, album in enumerate(albumes):
        if album["id"] == id_album:
            del albumes[i]
            print("Álbum eliminado correctamente.")
            return
    print("No se encontró un álbum con ese ID.")

def mostrar_album(album):
    print(f"\nID: {album['id']}")
    print(f"Título: {album['titulo']}")
    print(f"Artista: {album['artista']}")
    print(f"Género: {album['genero'].capitalize()}")
    print(f"Año: {album['anio']}")
    print(f"Formato: {album['formato'].capitalize()}")
    print(f"Stock - Vinilo: {album['stock_vinilo']}, CD: {album['stock_cd']}, Digital: {album['stock_digital']}")

def mostrar_todos():
    if albumes:
        for album in albumes:
            mostrar_album(album)
    else:
        print("No hay álbumes registrados.")


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


