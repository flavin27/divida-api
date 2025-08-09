from App.DTOs.cdaDTO import CdaDTO
from App.DTOs.Dw.dim_dataDTO import DimDataDTO

class DimDataParser:

    def __init__(self):
        self.data = []
        self.datas_existentes = set()  
    
    def parse_cda_data(self, cda_data: list[CdaDTO]) -> list[DimDataDTO]:

        for item in cda_data:
            for data in [item.data_situacao, item.data_cadastramento]:
                if data and data not in self.datas_existentes:
                    dto = DimDataDTO(
                        data=data,
                        ano=data.year,
                        mes=data.month,
                        dia=data.day,
                        trimestre=(data.month - 1) // 3 + 1,
                        semana=data.isocalendar()[1],
                        dia_semana=data.weekday()
                    )
                    self.data.append(dto)
                    self.datas_existentes.add(data)

        return self.data
