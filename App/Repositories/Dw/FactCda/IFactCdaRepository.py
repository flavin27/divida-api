from abc import ABC, abstractmethod
from typing import Dict, List
from App.DTOs.cdaDTO import CdaDTO
from App.Http.Requests.CdaResquest import CdaRequest

class IFactCdaRepository(ABC):

    @abstractmethod
    def save_all(self, situacoes: List[CdaDTO]) -> None:
        pass


    def get_all(self) -> Dict[str,int]:
        pass

    @abstractmethod
    def get_id_by_cda(self, cda: CdaDTO) -> int:
        pass

    @abstractmethod
    def index(self, request: CdaRequest) -> List[object]:
        pass

    @abstractmethod
    def get_distribuicao_cdas():
        pass

    @abstractmethod
    def get_inscricoes():
        pass

    @abstractmethod
    def get_montante():
        pass
