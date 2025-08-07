import pandas as pd
from App.DTOs.recuperacaoDTO import RecuperacaoDTO

from Database.Parsers.baseParser import BaseParser

class RecuperacaoParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()

        recuperacaoList = []

        

        for _, row in df.iterrows():

            num_cda = row['numCDA']
            if isinstance(row['numCDA'], int ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])
            if isinstance(row['numCDA'], float ) and len(str(row['numCDA'])) > 2:
                num_cda = str(row['numCDA'])[0:-2]

            obj = RecuperacaoDTO(
                num_cda = num_cda,
                prob_recuperacao = row['probRecuperacao'],
                sts_recuperacao = row['stsRecuperacao'],
            )
            recuperacaoList.append(obj)

        return recuperacaoList

def run():
    parser = RecuperacaoParser('data/004.csv')
    parsed_data = parser.parse()
    for item in parsed_data:
        print(item)

if __name__ == "__main__":
    run()


