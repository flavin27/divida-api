from abc import ABC, abstractmethod
from typing import List
from App.DTOs.cda_pessoaDTO import CdaPessoaDTO

class ICdaPessoaRepository(ABC):

    @abstractmethod
    def save_all(self, cda_pessoas: List[CdaPessoaDTO]) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[CdaPessoaDTO]:
        pass

    @abstractmethod
    def get_all_with_document(self) -> List[CdaPessoaDTO]:
        pass



