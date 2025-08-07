from abc import ABC, abstractmethod
from typing import List
from App.DTOs.situacaoCdaDTO import SituacaoCdaDTO

class ISituacaoCdaRepository(ABC):

    @abstractmethod
    def save_all(self, situacoes: List[SituacaoCdaDTO]) -> None:
        pass

