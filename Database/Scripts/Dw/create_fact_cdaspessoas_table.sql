CREATE TABLE fact_cdas_pessoas (
    id SERIAL PRIMARY KEY,
    cda_id INTEGER NOT NULL,
    pessoa_id INTEGER NOT NULL,
    sitacao_devedor VARCHAR NOT NULL,
    CONSTRAINT fk_cda FOREIGN KEY (cda_id) REFERENCES fact_cdas(id),
    CONSTRAINT fk_pessoa FOREIGN KEY (pessoa_id) REFERENCES dim_pessoas(id)
);
