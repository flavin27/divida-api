CREATE TABLE situacao_cdas (
    cod_situacao_cda INTEGER PRIMARY KEY,
    nome VARCHAR NOT NULL,
    cod_situacao_fiscal INTEGER NOT NULL,
    cod_fase_cobranca INTEGER NOT NULL,
    cod_exigibilidade INTEGER NOT NULL,
    tipo VARCHAR NOT NULL
);
