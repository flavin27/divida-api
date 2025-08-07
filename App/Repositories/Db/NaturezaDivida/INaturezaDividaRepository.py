from abc import ABC, abstractmethod
from typing import List
from App.DTOs.naturezaDividaDTO import NaturezaDividaDTO

class INaturezaDividaRepository(ABC):

    @abstractmethod
    def save_all(self, naturezas: List[NaturezaDividaDTO]) -> None:
        pass
