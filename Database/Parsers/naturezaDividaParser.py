import pandas as pd
from App.DTOs.naturezaDividaDTO import NaturezaDividaDTO

from Database.Parsers.baseParser import BaseParser

class NaturezaDividaParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()
        df = df.drop_duplicates(subset=["idNaturezadivida"], keep="first")

        naturezaDividaList = []

        for _, row in df.iterrows():
            obj = NaturezaDividaDTO(
                id=row['idNaturezadivida'],
                nome=row['nomnaturezadivida'],
                descricao=row['descnaturezadivida']
            )
            naturezaDividaList.append(obj)

        return naturezaDividaList



