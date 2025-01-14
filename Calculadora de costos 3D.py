print ("******* CALCULADORA DE COSTOS *******")
print ("*******   PARA BAMBULAB A1    *******")

def datos ():
    hs = int(input("¿Cuantas horas dura la impresion?:"))
    min = int(input("¿Cuantos minutos dura la impresion?:"))
    gr = int(input("¿Cuantos gramos va a consumir?"))
    arg = int(input("¿Cuantas argollas para llavero va a utilizar?"))
    return hs, min, gr, arg

def calculos (hs, min, gr, arg):
    amortizacion = (1500000/10000) * (hs+(min/60)) #Precio de la impresora dividido hora de vida util
    costo_en_gramos = (13500/1000) * gr #Precio de filamento dividido en 1000gr
    costo_en_argollas = 700 * arg #Precio de argolla * cant de argollas
    costo_total = amortizacion + costo_en_gramos + costo_en_argollas
    return costo_total

def ganancia (costo):
    while True:
        porcentaje = int(input("Porcentaje de ganancia:"))
        precio_venta = (porcentaje/100) * costo + costo
        print(f"Total de costos {costo}")
        print(f"Precio de venta sugerido ${precio_venta}")
        opc = int(input("Seleccione 1 para salir o cualquier otro numero para elegir otro %"))
        
        if opc == 1:
            break

hr, min, gr, arg = datos()

costo = calculos(hr, min, gr, arg)

ganancia(costo)