from abc import ABC, abstractmethod
import pandas as pd

class BaseParser(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def parse(self) -> list:
        pass

    def read_csv(self):
        return pd.read_csv(self.path)
