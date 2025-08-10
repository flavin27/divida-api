from abc import ABC, abstractmethod
from typing import Dict, List
from App.DTOs.cda_pessoaDTO import CdaPessoaDTO

class IFactCdaPessoaRepository(ABC):
    @abstractmethod
    def save_all(self, cda_pessoas: List[CdaPessoaDTO]) -> None:
        pass
