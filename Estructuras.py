import numpy as np
import math

class dinamico():

    def __init__(self):
        self.espacio=1
        self.tam=0
        self.arreglo=np.empty(self.espacio,dtype=int)
    
    def __len__(self):
        return self.tam
        
    def add(self, nuevo):
        if self.tam<self.espacio:
            self.arreglo[self.tam]=nuevo
            self.tam+=1
        else:
                self.espacio*=2
                newA=np.empty(self.espacio, dtype=int)
                for i in range(self.tam):
                    newA[i]=self.arreglo[i]
                newA[self.tam]=nuevo
                self.tam+=1
                self.arreglo=newA
                
    
    def __str__(self):
        print("Espacio: {0}\tElementos:{1}".format(self.espacio,self.tam))
        return"--".join([str(x) for x in self.arreglo[:self.tam]])
        
    def __getitem__(self,pos):
        if 0<=pos<self.tam:
            return self.arreglo[pos]
        else:
            raise IndexError
                
    def lastDie(self):
        x=self.tam-1
        if x<= (self.espacio)*(0.5):
            self.espacio=math.floor((self.espacio)*(3/4))
        newA=np.empty(self.espacio, dtype=int)
        self.tam-=1
        for i in range(self.tam):
            newA[i]=self.arreglo[i]
        self.arreglo=newA