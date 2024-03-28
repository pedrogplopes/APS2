from abc import ABC, abstractmethod

class PedidoState(ABC):
    @abstractmethod
    def confirmar_pedido(self):
        pass
    
    @abstractmethod
    def preparar_pedido(self):
        pass
    
    @abstractmethod
    def entregar_pedido(self):
        pass
    
    @abstractmethod
    def cancelar_pedido(self):
        pass