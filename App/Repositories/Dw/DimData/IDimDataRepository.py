from abc import ABC, abstractmethod
from typing import List
from App.DTOs.Dw.dim_dataDTO import DimDataDTO


class IDimDataRepository(ABC):

    @abstractmethod
    def save_all(self, situacoes: List[DimDataDTO]) -> None:
        pass

    @abstractmethod
    def save(self, data: DimDataDTO) -> int:
        pass

    @abstractmethod
    def get_id_by_data(self, data: str) -> int:
        pass