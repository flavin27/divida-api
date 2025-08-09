CREATE TABLE historico_cdas (
    id SERIAL PRIMARY KEY,
    num_cda VARCHAR NOT NULL,
    ano_inscricao INTEGER NOT NULL,
    id_natureza_divida INTEGER NOT NULL,
    cod_situacao_cda INTEGER NOT NULL,
    data_situacao DATE NOT NULL,
    cod_fase_cobranca VARCHAR NOT NULL,
    data_cadastramento DATE NOT NULL,
    valor_saldo NUMERIC(15, 2) NOT NULL,
    FOREIGN KEY(id_natureza_divida) REFERENCES natureza_dividas (id),
    FOREIGN KEY(cod_situacao_cda) REFERENCES situacao_cdas (cod_situacao_cda)
);
