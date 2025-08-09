CREATE TABLE recuperacoes (
    num_cda VARCHAR PRIMARY KEY,
    prob_recuperacao FLOAT NOT NULL,
    sts_recuperacao VARCHAR NOT NULL,
    CONSTRAINT fk_recuperacoes_num_cda FOREIGN KEY (num_cda)
        REFERENCES cdas (num_cda)
        ON DELETE CASCADE
);
