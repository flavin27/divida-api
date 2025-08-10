from abc import ABC, abstractmethod
from typing import List, Dict
from App.DTOs.pessoaDTO import PessoaDTO

class IDimPessoaRepository(ABC):

    @abstractmethod
    def save_all(self, pessoas: List[PessoaDTO]) -> None:
        pass

    @abstractmethod
    def get_all(self) -> Dict[int, int]:
        pass

    @abstractmethod
    def index(self) -> List[PessoaDTO]:
        pass


