CREATE TABLE fact_cdas (
    id SERIAL PRIMARY KEY,
    num_cda VARCHAR NOT NULL,
    natureza_id INTEGER NOT NULL,
    situacao_id INTEGER NOT NULL,
    ano_inscricao_id INTEGER NOT NULL,
    data_situacao_id INTEGER NOT NULL,
    data_cadastramento_id INTEGER NOT NULL,
    cod_fase_cobranca VARCHAR NOT NULL,
    valor_saldo NUMERIC(15, 2) NOT NULL,
    CONSTRAINT fk_natureza FOREIGN KEY (natureza_id) REFERENCES dim_natureza_dividas(id),
    CONSTRAINT fk_situacao FOREIGN KEY (situacao_id) REFERENCES dim_situacao_cdas(id),
    CONSTRAINT fk_ano_inscricao FOREIGN KEY (ano_inscricao_id) REFERENCES dim_datas(id),
    CONSTRAINT fk_data_situacao FOREIGN KEY (data_situacao_id) REFERENCES dim_datas(id),
    CONSTRAINT fk_data_cadastramento FOREIGN KEY (data_cadastramento_id) REFERENCES dim_datas(id)
);
