ContraseñasRegistradas = []
TipoDeUsuarioPermitido = ["F","M"]
UsuarioRegistrado = []
Registrogen = []
def menu():
        print("MENU PRINCIPAL")
        print("1. Ingresar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
def ingresarusuario():
    NombreUsuario = input("Ingrese El Nombre Del Usuario: ")
    TipoDeUsuarioaRegristar = input("Ingrese Sexo: ")
    if TipoDeUsuarioaRegristar not in TipoDeUsuarioPermitido:
        print("Debe Ingresar F o M solamente. Intente Denuevo")
    else:
        Contraseña = input("Ingrese Su Contraseña: ")
        ContraseñasRegistradas.append(Contraseña)
        UsuarioRegistrado.append(NombreUsuario)
        Registrogen.append(TipoDeUsuarioaRegristar)
        print("Usuario Registrado Con Exito!!")
def buscarusuario():
    BuscaDeUsuario = input("Ingrese usuario a buscar : ")
    if BuscaDeUsuario in UsuarioRegistrado:
        print(f"El Sexo Del Usuario Es {Registrogen} y la contraseña es {ContraseñasRegistradas}")
    else:
        print("El usuario no se encuentra registrado")
def eliminarusuari():
    UsuarioABuscar = input("Ingrese El Usuario a Buscar: ")
    if UsuarioABuscar in UsuarioRegistrado:
        UsuarioRegistrado.remove(UsuarioABuscar)
        print("Usuario eliminado Con Exito!!")
    else:
        print("No Se Pudo Eliminar el usuario!!")
def salir():
    print("Programa Terminado...")
            
            