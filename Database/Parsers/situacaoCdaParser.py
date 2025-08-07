import pandas as pd
from App.DTOs.situacaoCdaDTO import SituacaoCdaDTO

from Database.Parsers.baseParser import BaseParser

class SituacaoCdaParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()

        situacaoCdaList = []

        for _, row in df.iterrows():
            obj = SituacaoCdaDTO(
                cod_situacao_cda=row['codSituacaoCDA'],
                nome=row['nomSituacaoCDA'],
                cod_situacao_fiscal=row['codSituacaoFiscal'],
                cod_fase_cobranca=row['codFaseCobranca'],
                cod_exigibilidade=row['codExigibilidade'],
                tipo=row['tipoSituacao']
            )
            situacaoCdaList.append(obj)

        return situacaoCdaList


if __name__ == "__main__":
    parser = SituacaoCdaParser('data/003.csv')
    situacao_cdas = parser.parse()
    for situacao in situacao_cdas:
        print(situacao)



