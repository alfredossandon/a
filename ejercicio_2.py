# Escriba un programa que pida dos palabras y diga si riman o no. 
# Si coinciden las últimas tres letras tiene que decir que riman. 
# Si coinciden sólo las últimas dos tiene que decir que riman un poco. 
# Y si no coinciden, decir que no riman. 
# Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices

def main():
    palabra1 = input("Escriba una palabra: ")
    palabra2 = input("Ingrese una segunda palabra: ")

    if palabra1 [-3:] == palabra2 [-3:]:
        print("Sus palabras si riman.")
    elif palabra1 [-2:] == palabra2 [-2:]:
        print("Sus palabras riman un poco.")
    else:
        print("Sus palabras no riman.")



if __name__ == '__main__':
    main()

