from abc import ABC, abstractmethod
from typing import Dict, List
from App.DTOs.cdaDTO import CdaDTO

class IFactCdaRepository(ABC):

    @abstractmethod
    def save_all(self, situacoes: List[CdaDTO]) -> None:
        pass


    def get_all(self) -> Dict[str,int]:
        pass

    @abstractmethod
    def get_id_by_cda(self, cda: CdaDTO) -> int:
        pass
