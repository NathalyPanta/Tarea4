
class Listita:
    def __init__(self, tamaniox=3):
        self.lista=[]
        self.longitud = 0 
        self.size = tamaniox
        
    def append(self,dato):
        if self.longitud<self.size:
            self.lista += [dato]
            self.longitud += 1
            return True
        else:
            return False
    
    def obtener(self,pos):
        if pos < 0 or pos >=self.longitud:
            return None
        else:
            x = print("La posición {} tiene como valor {}" .format(pos,self.lista[pos]))
            return x
        
    def presentareliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado = self.lista [pos]
            self.lista = self.lista [:pos] + self.lista [pos+1:]
            print("Su lista es: {}. El elemento que fue eliminado es {}" .format (self.lista,eliminado))

    def buscar_valor (self,valor):
        if valor in self.lista:
            self.frsd = self.lista.index(valor)
            print("La posición del dato es ", self.frsd)
            return True
        else:
            return False
        
    def adiciona_v (self, valor):
        if self.buscar_valor(valor) == False:
            self.size +=1
            self.append(valor)
            return self.lista
        
    def eliminar (self,valor):
        if self.buscar_valor(valor) == True:
            self.presentareliminado(self.frsd)
        else:
            False
    
    def mostrar(self):
        print("{:3}{:9}{}" .format ("","lista","posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:10}] {:3}" .format(ele,pos))
        
    
        