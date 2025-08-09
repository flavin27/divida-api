CREATE TABLE cdas_pessoas (
    num_cda VARCHAR NOT NULL,
    id_pessoa INTEGER NOT NULL,
    sitacao_devedor VARCHAR NOT NULL,
    PRIMARY KEY (num_cda, id_pessoa),
    CONSTRAINT fk_cdas_pessoas_num_cda FOREIGN KEY (num_cda)
        REFERENCES cdas (num_cda)
        ON DELETE CASCADE,
    CONSTRAINT cdas_pessoas_id_pessoa_fkey FOREIGN KEY (id_pessoa)
        REFERENCES pessoas (id)
);
