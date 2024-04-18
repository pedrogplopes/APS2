from __future__ import annotations
from collections.abc import Iterator
from typing import Any, List, Optional

class Produto:
    def __init__(self, nome: str, categoria: str, valor: float) -> None:
        self.nome = nome
        self.categoria = categoria
        self.valor = valor

class ProdutoIterator(Iterator):
    def __init__(self, produtos: List[Produto]) -> None:
        self.produtos = sorted(produtos, key=lambda p: (p.categoria, p.valor))
        self.index = 0

    def __next__(self) -> Optional[Produto]:
        if self.index < len(self.produtos):
            produto = self.produtos[self.index]
            self.index += 1
            return produto
        else:
            raise StopIteration
