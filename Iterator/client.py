from products import Produto, ProdutoIterator

class Cliente:
    def main(self):
        produtos = [
            Produto("Prod1", "A", 99.9),
            Produto("Prod2", "B", 19.9),
            Produto("Prod3", "A", 29.9),
            Produto("Prod4", "C", 49.9),
            Produto("Prod5", "A", 9.9),
            Produto("Prod6", "B", 59.9),
            Produto("Prod7", "C", 39.9),
            Produto("Prod8", "A", 79.9),
            Produto("Prod9", "B", 69.9),
            Produto("Prod10", "C", 89.9),
        ]

        iterator = ProdutoIterator(produtos)
        for produto in iterator:
            print(f"Produto: {produto.nome}, Categoria: {produto.categoria}, Valor: R${produto.valor}")


if __name__ == "__main__":
    cliente = Cliente()
    cliente.main()
