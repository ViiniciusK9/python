class Caneta:
    def __init__(self, marca, cor, ponta, carga, tampada=True, escrevendo=False):
        # ATRIBUTOS
        self._marca = marca
        self._cor = cor
        self._ponta = ponta
        self.carga = carga 
        self.tampada = tampada 
        self.escrevendo = escrevendo

    # METODO
    def destampar(self):
        if (not self.tampada):
            print("A caneta já está destampada.")
            return

        print("A caneta foi destampada.")
        self.tampada = False
    

    def tampar(self):
        if (self.tampada):
            print("A caneta já está tampada.")
            return

        print("A caneta foi tampada.")
        self.tampada = True
    

    def escrever(self, texto):
        if (self.escrevendo):
            print("A caneta já está escrevendo.")
            return
        
        print(f"Escrevendo: {texto}")
        self.escrevendo = True

    
    def parar_escrever(self):
        if (not self.escrevendo):
            print("A caneta não está escrevendo.")
            return
        
        print("A caneta parou de escrever.")
    
    # GETTER
    @property
    def marca(self):
        #print("passou pelo getter")
        return self._marca

    # SETTER
    @marca.setter
    def marca(self, valor):
        #print("passou pelo setter")
        self._marca = valor
    

    @property
    def cor(self):
        return self._cor


    @cor.setter
    def cor(self, valor):
        self._cor = valor

    
    @property
    def ponta(self):
        return self._ponta


    @ponta.setter
    def ponta(self, valor):
        self._ponta = valor
