class Colitas:
    def __init__(self,tamaniox=3):
        self.lista = []
        self.size = tamaniox
        self.top = 0

    def insentar(self,dato):
        if self.top < self.size:
            self.lista += [dato]
            self.top += 1
            return True
        else:
            return False

    def quitar(self): 
        if self.empty():
            return None
        else:
            pri = self.lista.pop(0)
            self.top -= 1
            return pri

    def empty(self):
         if self.top == 0:
            return True
         else:
            return False

    def mostrar(self):
        for top in range(self.top):
            print("[{}]".format(self.lista[top]))

    def longitud(self):
        return self.top