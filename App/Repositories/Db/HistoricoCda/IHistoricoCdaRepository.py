from abc import ABC, abstractmethod
from typing import List
from App.DTOs.cdaDTO import CdaDTO

class IHistoricoCdaRepository(ABC):

    @abstractmethod
    def save_all(self, cdas: List[CdaDTO]) -> None:
        pass


