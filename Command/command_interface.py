from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# O padrão Command permite a parametrização de operações ao encapsular solicitações como objetos. 
# Cada comando é implementado como uma classe separada que implementa uma interface comum.
# Isso permite passar diferentes comandos para o invoker sem alterá-lo.
# Além disso, o padrão command dá suporte para reversão pois suas solicitações são feitas de forma enfileirada.
# Para reverter ações, basta percorrer a fila desfazendo comandos em ordem inversa.