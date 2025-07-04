from Work import menu,ingresarusuario,buscarusuario,eliminarusuari,salir
ContraseñasRegistradas = []
TipoDeUsuarioPermitido = ["F","M"]
UsuarioRegistrado = []
Registrogen = []
while True:
    menu()
    OpcionIngresada = int(input("Ingrese Opcion: "))
    if OpcionIngresada == 1:
        ingresarusuario()
    elif OpcionIngresada == 2:
        buscarusuario()
    elif OpcionIngresada == 3:
        eliminarusuari()
    elif OpcionIngresada == 4:
        salir()
        break
    else:
        print("Debe Ingresar Una Opcion Valida!!")