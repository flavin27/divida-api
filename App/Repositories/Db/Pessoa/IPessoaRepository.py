from abc import ABC, abstractmethod
from typing import List, Dict
from App.DTOs.pessoaDTO import PessoaDTO

class IPessoaRepository(ABC):

    @abstractmethod
    def save_all(self, pessoas: List[PessoaDTO]) -> None:
        pass
    @abstractmethod
    def get_all(self) -> List[PessoaDTO]:
        pass

    @abstractmethod
    def get_all_as_map(self) -> Dict[str, int]:
        pass


