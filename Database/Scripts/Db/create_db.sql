-- natureza_dividas definição

-- DROP TABLE IF EXISTS natureza_dividas CASCADE;

CREATE TABLE natureza_dividas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    descricao VARCHAR
);

-- Enum documentenum substituído por CHECK constraint em pessoas

-- pessoas definição

-- DROP TABLE IF EXISTS pessoas CASCADE;

CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    documento VARCHAR,
    tipo_documento VARCHAR(20) NOT NULL CHECK (tipo_documento IN ('CPF', 'CNPJ', 'RG', 'PASSAPORTE'))
);

-- situacao_cdas definição

-- DROP TABLE IF EXISTS situacao_cdas CASCADE;

CREATE TABLE situacao_cdas (
    cod_situacao_cda INTEGER PRIMARY KEY,
    nome VARCHAR NOT NULL,
    cod_situacao_fiscal INTEGER NOT NULL,
    cod_fase_cobranca INTEGER NOT NULL,
    cod_exigibilidade INTEGER NOT NULL,
    tipo VARCHAR NOT NULL
);

-- cdas definição

-- DROP TABLE IF EXISTS cdas CASCADE;

CREATE TABLE cdas (
    num_cda VARCHAR PRIMARY KEY,
    ano_inscricao INTEGER NOT NULL,
    id_natureza_divida INTEGER NOT NULL,
    cod_situacao_cda INTEGER NOT NULL,
    data_situacao DATE NOT NULL,
    cod_fase_cobranca VARCHAR NOT NULL,
    data_cadastramento DATE NOT NULL,
    valor_saldo NUMERIC(15, 2) NOT NULL,
    CONSTRAINT fk_cdas_cod_situacao_cda FOREIGN KEY (cod_situacao_cda) REFERENCES situacao_cdas(cod_situacao_cda),
    CONSTRAINT fk_cdas_id_natureza_divida FOREIGN KEY (id_natureza_divida) REFERENCES natureza_dividas(id)
);

-- cdas_pessoas definição

-- DROP TABLE IF EXISTS cdas_pessoas CASCADE;

CREATE TABLE cdas_pessoas (
    num_cda VARCHAR NOT NULL,
    id_pessoa INTEGER NOT NULL,
    sitacao_devedor VARCHAR NOT NULL,
    CONSTRAINT pk_cdas_pessoas PRIMARY KEY (num_cda, id_pessoa),
    CONSTRAINT fk_cdas_pessoas_id_pessoa FOREIGN KEY (id_pessoa) REFERENCES pessoas(id),
    CONSTRAINT fk_cdas_pessoas_num_cda FOREIGN KEY (num_cda) REFERENCES cdas(num_cda) ON DELETE CASCADE
);

-- historico_cdas definição

-- DROP TABLE IF EXISTS historico_cdas CASCADE;

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
    CONSTRAINT fk_historico_cdas_cod_situacao_cda FOREIGN KEY (cod_situacao_cda) REFERENCES situacao_cdas(cod_situacao_cda),
    CONSTRAINT fk_historico_cdas_id_natureza_divida FOREIGN KEY (id_natureza_divida) REFERENCES natureza_dividas(id)
);

-- recuperacoes definição

-- DROP TABLE IF EXISTS recuperacoes CASCADE;

CREATE TABLE recuperacoes (
    num_cda VARCHAR PRIMARY KEY,
    prob_recuperacao DOUBLE PRECISION NOT NULL,
    sts_recuperacao VARCHAR NOT NULL,
    CONSTRAINT fk_recuperacoes_num_cda FOREIGN KEY (num_cda) REFERENCES cdas(num_cda) ON DELETE CASCADE
);
