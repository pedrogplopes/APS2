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

class AguardandoConfirmacao(PedidoState):
    def __init__(self, pedido):
        self.pedido = pedido

    def confirmar_pedido(self):
        print("Pedido confirmado pelo restaurante.")
        self.pedido.set_state(EmPreparo(self.pedido))

    def preparar_pedido(self):
        print("O pedido ainda não foi confirmado pelo restaurante.")

    def entregar_pedido(self):
        print("O pedido ainda não foi confirmado pelo restaurante.")

    def cancelar_pedido(self):
        print("Pedido cancelado.")
        self.pedido.set_state(Cancelado(self.pedido))

class EmPreparo(PedidoState):
    def __init__(self, pedido):
        self.pedido = pedido

    def confirmar_pedido(self):
        print("O pedido já está em preparo.")

    def preparar_pedido(self):
        print("Pedido em preparo.")
        self.pedido.set_state(ProntoParaEntrega(self.pedido))

    def entregar_pedido(self):
        print("O pedido ainda não está pronto para entrega.")

    def cancelar_pedido(self):
        print("Pedido cancelado.")
        self.pedido.set_state(Cancelado(self.pedido))

class ProntoParaEntrega(PedidoState):
    def __init__(self, pedido):
        self.pedido = pedido

    def confirmar_pedido(self):
        print("O pedido já está pronto para entrega.")

    def preparar_pedido(self):
        print("O pedido já está pronto para entrega.")

    def entregar_pedido(self):
        print("Pedido entregue.")
        self.pedido.set_state(Entregue(self.pedido))

    def cancelar_pedido(self):
        print("Pedido cancelado.")
        self.pedido.set_state(Cancelado(self.pedido))

class Entregue(PedidoState):
    def __init__(self, pedido):
        self.pedido = pedido

    def confirmar_pedido(self):
        print("O pedido já foi entregue.")

    def preparar_pedido(self):
        print("O pedido já foi entregue.")

    def entregar_pedido(self):
        print("O pedido já foi entregue.")

    def cancelar_pedido(self):
        print("Não é possível cancelar um pedido já entregue.")

class Cancelado(PedidoState):
    def __init__(self, pedido):
        self.pedido = pedido

    def confirmar_pedido(self):
        print("Não é possível confirmar um pedido cancelado.")

    def preparar_pedido(self):
        print("Não é possível preparar um pedido cancelado.")

    def entregar_pedido(self):
        print("Não é possível entregar um pedido cancelado.")

    def cancelar_pedido(self):
        print("O pedido já está cancelado.")
