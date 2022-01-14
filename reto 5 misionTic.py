def calculadoraMes(registroDeAhorros,nombre):
    #separacion de los elementos por cada ";" que encuentre
    registroDeAhorros=registroDeAhorros.split(';')
    y=0
    res={}
    for i in registroDeAhorros:
        #a X le doy el valor de cada valor que fue separado anteriormente
        x=registroDeAhorros[y]
        #X ya tiene valores separados, ahora separamos esos valores por cada "," que encuentre
        x=x.split(',')
        p=0
        res[x[0]]=0
        #ciclo para que me recorra la cantidad de elementos que hay en X (ya estan separados los meses y los ahorros)
        for q in range (1, len(x)):
            res[x[0]]+=eval(x[q])
        y+=1
        lista_final=(nombre,res)
    return (lista_final)

registroDeAhorros="Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4"
nombre="Daniel"
print (calculadoraMes(registroDeAhorros,nombre))