import matriz

def main():
    
    lista = ['CALCULATOR MATRIX\n\n''1. Determinante', '2. Transpuesta', '3. inversa', '4. Mult x # de matriz', '5. Elevada_potencia', '6. Simetrica', '7. Identidad',
             '8. Multiplicacion', '9. Suma', '10. Resta', '11. Salir']

    for i in lista:
        print i
    a = int(input("Selecione una opcion del 1 al 11 >>: "))
    if a == 1:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.determinante(a)

    if a == 2:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.transpuesta()

    if a == 3:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.inversa(a)

    if a == 4:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.numero()
    if a == 5:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.elevada()

    if a == 6:
         matrizA = matriz.Matriz()
         matrizA.simetrica()

    if a == 7:
         matrizA = matriz.Matriz()
         matrizA.identidad()

    if a == 8:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.multiplicacion(filasA, columnasB, filasB, columnasA, a, b)

    if a == 9:
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

        matrizB = matriz.Matriz()
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprime_matrizC()

        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()
        matrizA.resta(filasA, columnasB, filasB, columnasA, a, b)

    if a == 10:
        matrizA = matriz.Matriz()
        matrizA.crearMatrizA()
        a = matrizA.llenarmatrizA()
        matrizA.imprime_matriz()
        columnasA = matrizA.getColumnas()
        filasA = matrizA.getFilas()

        matrizB = matriz.Matriz()
        matrizB.crearMatrizA()
        b = matrizB.llenarmatrizA()
        matrizB.imprime_matrizC()

        columnasB = matrizB.getColumnas()
        filasB = matrizB.getFilas()
        matrizA.suma(filasA, columnasB, filasB, columnasA, a, b)

        if a == 11:
            print "Hasta la Proxima: "
        exit = True

if __name__ == '__main__':
    main()