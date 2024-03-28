from orders import Pedido, CentralPedidos

if __name__ == "__main__":
    pedido = Pedido()
    central_pedidos = CentralPedidos(pedido)

    central_pedidos.confirmar_pedido()
    central_pedidos.preparar_pedido()
    central_pedidos.entregar_pedido()
    central_pedidos.cancelar_pedido()
