class arbolBinario:
    raiz=None
    izq=None
    der=None
    indice=0
    miLista=None

    def init(self):
        raiz = None
        izq = None
        der = None
        indice=0
        miLista = [1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16384,32768]
        print("Se creo un arbol Binario")

    def queNivel(self, numero):
        res=-1
        i=0
        encontro=False
        while encontro==False:
            if numero<=miLista[i]:
                res=i
                encontro=True
            i=i+1
        return res

    def agregar(self, dato):
        indiceActual = self.indice + 1
        self.indice = self.indice + 1
        self.agregarChido(self,dato,indiceActual)
    
    
    def agregarChido(self, arbol, dato, ini):
        if ini==1:
            arbol.raiz = dato
            print("Se inserto el dato: ",dato)
        else:
            if ini==2:
                izq = arbolBinario()
                izq.raiz = dato
                print("Se inserto el dato: ",dato)
            else:
                if ini==3:
                    der = arbolBinario()
                    der.raiz = dato
                    print("Se inserto el dato: ",dato)
                else:
                    nivel = queNivel(dato)
                    ini = ini - (2**nivel)
                    estaIzq = estaEnLaIzq(nivel,dato)
                    if estaIzq:
                        izq.agregarChido(izq,dato,ini)
                    else:
                        der.agregarChido(der,dato.ini)
    
    # Este metodo esta usando elif, estos son mas entendible
    # Lamentablemente este no se usa
    def agregarChido2(self, arbol, dato, ini):
        if ini == 1:
            arbol.raiz = dato
            print("Se inserto el dato: ",dato)
        elif ini == 2:
            izq = arbolBinario()
            izq.raiz = dato
            print("Se inserto el dato: ",dato)
        elif ini == 3:
            der = arbolBinario()
            der.raiz = dato
            print("Se inserto el dato: ",dato)
        else:
            nivel = queNivel(dato)
            ini = ini - (2**nivel)
            estaIzq = estaEnLaIzq(nivel,dato)
            if estaIzq:
                izq.agregarChido(izq,dato,ini)
            else:
                der.agregarChido(der,dato.ini)

    def estaEnLaIzq(self, niv, dat):
        resp = False
        medio = (miLista[niv]+miLista[niv-1])/2
        if dat<=medio:
            resp = True
        return resp

    def getIndice(self):
        return self.indice


def mostrar():
    arbolito = arbolBinario()
    arbolito.agregar("Hola")
    tamanio = arbolito.getIndice()
    print(tamanio)

mostrar()