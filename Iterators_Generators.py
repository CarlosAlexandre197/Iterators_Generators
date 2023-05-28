'''Exemplo001'''

#Iterators

class Fibonacci:

    def _init_(self, maximo=1000000):
        self.elementoAtual, self.proxElemento = 0, 1
        self.maximo = maximo

    def _iter_(self):
        return self
    
    def _next_(self):
        if self.elementoAtual > self.maximo:
            raise StopIteration
        
        valorRetorno = self.elementoAtual
        self.elementoAtual, self.proxElemento = self.proxElemento, self.elementoAtual + self.proxElemento

        return valorRetorno
    
'''Exemplo002'''

#Generators

def Fibonacci(maximo):

    elementoAtual, proximoElemento = 0, 1

    while elementoAtual < maximo:
        yield elementoAtual

        elementoAtual, proximoElemento = proximoElemento, elementoAtual + proximoElemento
        
