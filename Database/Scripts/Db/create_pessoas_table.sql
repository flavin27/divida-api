CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR NOT NULL,
    documento VARCHAR,
    tipo_documento VARCHAR NOT NULL CHECK (tipo_documento IN ('CPF', 'CNPJ'))
);
