#En caso de duda,
#Para reemplazar caracteres pueden usar:
#cadena.replace(caracter_a_reemplazar, "")

#Para contar ocurrencias dentro de una lista:
#lista.count(elemento)

#Ingreso de datos del usuario
parrafo=input("Ingrese un parrafo que contenga minino 100 palabras: ")
palabras=parrafo.split()
longitud=len(palabras)
print("El parrafo tiene una longitud de: ", longitud)


espacios=0
numeros=0
signos=0
suma=0

for i in range(0,longitud):
    if (parrafo[i].isspace()): 
        espacios+=1
    elif(parrafo[i].isdigit()):
        numeros+=1
    elif(parrafo[i] in "?¡¿*,.-_:'"): #agrego los signos a discriminar (no se si hay un método)
        signos+=1

    suma=espacios+numeros+signos #sumo los contadores

rpta=longitud-suma #al final solo lo resto a la longitud original
print("Unicamente de palabras (letras) contiene: ",rpta)

caracteres=[]

for l in palabras:
    letra=[]
    longitud=len(l)
    letra.append(l)
    letra.append(longitud)
    list(caracteres).append(longitud)
    caracteres.append(letra)
    caracteres.sort(key=lambda x:x[1],reverse= True)

print("La palabra con más caracteres es: ", " ".join(map(str,caracteres[0])))
print("La palabra con menos caracteres es: ", ",".join(map(str,caracteres[-1])))

        
    



