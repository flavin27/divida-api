from abc import ABC, abstractmethod
from typing import List
from App.DTOs.pessoaDTO import PessoaDTO

class IDimPessoaRepository(ABC):

    @abstractmethod
    def save_all(self, pessoas: List[PessoaDTO]) -> None:
        pass


