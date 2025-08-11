CREATE TABLE dim_situacao_cdas (
    id SERIAL PRIMARY KEY,
    cod_situacao_cda INTEGER NOT NULL UNIQUE,
    nome VARCHAR NOT NULL,
    cod_situacao_fiscal INTEGER NOT NULL,
    cod_fase_cobranca INTEGER NOT NULL,
    cod_exigibilidade INTEGER NOT NULL,
    tipo VARCHAR NOT NULL
);
