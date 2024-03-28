from concrete_states import AguardandoConfirmacao

class Pedido:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

class CentralPedidos:
    def __init__(self, pedido):
        self.pedido = pedido
        self.pedido.set_state(AguardandoConfirmacao(self.pedido))

    def confirmar_pedido(self):
        self.pedido.state.confirmar_pedido()

    def preparar_pedido(self):
        self.pedido.state.preparar_pedido()

    def entregar_pedido(self):
        self.pedido.state.entregar_pedido()

    def cancelar_pedido(self):
        self.pedido.state.cancelar_pedido()
