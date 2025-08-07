import numbers
import pandas as pd
from App.DTOs.cda_pessoaDTO import Cda_pessoaDTO

from Database.Parsers.baseParser import BaseParser

class CdaPessoaParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()

        cdaPessoaList = []

        

        for _, row in df.iterrows():

            num_cda = row['numCDA']
            if isinstance(row['numCDA'], numbers.Integral ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])
            if isinstance(row['numCDA'], float ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])[0:-2]
                

            obj = Cda_pessoaDTO(
                num_cda = num_cda,
                idPessoa = row['idPessoa'],
                sitacao_devedor = row['descsituacaodevedor'],
            )
            cdaPessoaList.append(obj)

        return cdaPessoaList

def run():
    parser = CdaPessoaParser('data/005.csv')
    parsed_data = parser.parse()
    for item in parsed_data:
        print(item)

if __name__ == "__main__":
    run()


