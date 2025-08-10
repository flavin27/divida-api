from abc import ABC, abstractmethod
from typing import List
from App.DTOs.recuperacaoDTO import RecuperacaoDTO

class IFactRecuperacaoRepository(ABC):
    @abstractmethod
    def save_all(self, recuperacoes: List[RecuperacaoDTO]) -> None:
        pass


