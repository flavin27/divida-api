import pandas as pd
from App.DTOs.pessoaDTO import PessoaDTO
from App.Enums.DocumentEnum import DocumentEnum
from Database.Parsers.baseParser import BaseParser

class PessoaParser(BaseParser):
    def __init__(self, path):
        super().__init__(path)

    def parse(self) -> list:
        df = self.read_csv()
        df = df.drop_duplicates(subset=["idpessoa"], keep="first")

        pessoaList = []

        for _, row in df.iterrows():
            cpf = row.get('numcpf')
            cnpj = row.get('numCNPJ')

            if pd.notna(cpf):
                documento = cpf
                tipo = DocumentEnum.CPF
            elif pd.notna(cnpj):
                documento = cnpj
                tipo = DocumentEnum.CNPJ
            else:
                continue  
            
            if isinstance(documento, float):
                documento = str(documento)[0:-2]
            
            if len(documento) not in [11, 14]:
                continue

            obj = PessoaDTO(
                id=row['idpessoa'],
                nome=row['descNome'],
                documento=documento,
                tipo_documento=tipo
            )

            pessoaList.append(obj)

        return pessoaList
    
if __name__ == "__main__":
    parser = PessoaParser('data/006.csv')
    pessoas = parser.parse()
    for pessoa in pessoas:
        print(pessoa)