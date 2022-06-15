# Escribir un programa que contenga una función que reciba una lista 
# de palabras y devuelva la más larga. 
# Imprimir por pantalla la palabra resultante.

def palabra_mas_larga(palabra):
    palabra_longitud = []
    for p in palabra:
        palabra_longitud.append((len(p), p))

    
    palabra_longitud.sort()
    return palabra_longitud[-1][1]

def main():
    palabra = ['Persona' , 'Paralelepipedo' , ' Perpendicular' , 'Justicia']    
    print(palabra_mas_larga(palabra))

if __name__ == '__main__':
    main()
