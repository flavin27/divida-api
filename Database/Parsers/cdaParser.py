import pandas as pd
from App.DTOs.cdaDTO import CdaDTO

from Database.Parsers.baseParser import BaseParser

class cdaParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()

        cdaList = []

        for _, row in df.iterrows():
            if isinstance(row['numCDA'], int ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])
            if isinstance(row['numCDA'], float ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])[0:-2]
            
            if row['ValSaldo'] < 0 or row['ValSaldo'] is None:
                continue

            obj = CdaDTO(
                num_cda = num_cda,
                ano_inscricao = row['anoInscricao'],
                id_natureza_divida = row['idNaturezaDivida'],
                cod_fase_cobranca = row['codFaseCobranca'],
                data_cadastramento = row['datCadastramento'],
                valor_saldo = row['ValSaldo'],
                cod_situacao_cda = row['codSituacaoCDA'],
                data_situacao = row['DatSituacao'],
            )
            cdaList.append(obj)

        return cdaList

def run():
    parser = cdaParser('data/001.csv')
    parsed_data = parser.parse()
    for item in parsed_data:
        print(item)

if __name__ == "__main__":
    run()



