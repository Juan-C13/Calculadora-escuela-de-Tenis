#Problema2
#Juan Esteban Clavijo García - 202225709

def calcularValoresEscuelaTenis(n,e,m):
    if e<12:
        c="Infantil"
        Vm=43000
    elif e<18:
        c="Juvenil"
        Vm=36000
    else:
        c="Mayores"
        Vm=32000
    T=Vm*m
    print("Nombre:",n)
    print("Categoria:",c)
    print("Valor a pagar:",T)
    print("")

calcularValoresEscuelaTenis("John Machado",15,5)
calcularValoresEscuelaTenis("Julieta Narvaez",11,2)
calcularValoresEscuelaTenis("Joaquín Beltrán",23,3)
