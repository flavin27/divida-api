CREATE TABLE fact_recuperacoes (
    id SERIAL PRIMARY KEY,
    num_cda VARCHAR NOT NULL,
    prob_recuperacao FLOAT NOT NULL,
    sts_recuperacao VARCHAR NOT NULL,
    cda_id INTEGER NOT NULL,
    CONSTRAINT fk_cda FOREIGN KEY (cda_id) REFERENCES fact_cdas(id)
);
