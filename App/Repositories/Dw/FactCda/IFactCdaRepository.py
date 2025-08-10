from abc import ABC, abstractmethod
from typing import List
from App.DTOs.cdaDTO import CdaDTO

class IFactCdaRepository(ABC):

    @abstractmethod
    def save_all(self, situacoes: List[CdaDTO]) -> None:
        pass
