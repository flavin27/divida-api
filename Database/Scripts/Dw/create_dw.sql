-- public.dim_datas definição

-- Drop table

-- DROP TABLE dim_datas;

CREATE TABLE dim_datas (
	id serial4 NOT NULL,
	"data" date NOT NULL,
	ano int4 NOT NULL,
	mes int4 NOT NULL,
	dia int4 NOT NULL,
	trimestre int4 NOT NULL,
	semana int4 NOT NULL,
	dia_semana int4 NOT NULL,
	CONSTRAINT dim_datas_data_key UNIQUE (data),
	CONSTRAINT dim_datas_pkey PRIMARY KEY (id)
);


-- public.dim_natureza_dividas definição

-- Drop table

-- DROP TABLE dim_natureza_dividas;

CREATE TABLE dim_natureza_dividas (
	id serial4 NOT NULL,
	nome varchar NOT NULL,
	descricao varchar NULL,
	CONSTRAINT dim_natureza_dividas_pkey PRIMARY KEY (id)
);


-- public.dim_pessoas definição

-- Drop table

-- DROP TABLE dim_pessoas;

CREATE TABLE dim_pessoas (
	id serial4 NOT NULL,
	nome varchar NOT NULL,
	documento varchar NULL,
	tipo_documento VARCHAR NOT NULL CHECK (tipo_documento IN ('CPF', 'CNPJ'))
	CONSTRAINT dim_pessoas_pkey PRIMARY KEY (id)
);


-- public.dim_situacao_cdas definição

-- Drop table

-- DROP TABLE dim_situacao_cdas;

CREATE TABLE dim_situacao_cdas (
	id serial4 NOT NULL,
	cod_situacao_cda int4 NOT NULL,
	nome varchar NOT NULL,
	cod_situacao_fiscal int4 NOT NULL,
	cod_fase_cobranca int4 NOT NULL,
	cod_exigibilidade int4 NOT NULL,
	tipo varchar NOT NULL,
	CONSTRAINT dim_situacao_cdas_cod_situacao_cda_key UNIQUE (cod_situacao_cda),
	CONSTRAINT dim_situacao_cdas_pkey PRIMARY KEY (id)
);


-- public.fact_cdas definição

-- Drop table

-- DROP TABLE fact_cdas;

CREATE TABLE fact_cdas (
	id serial4 NOT NULL,
	num_cda varchar NOT NULL,
	natureza_id int4 NOT NULL,
	situacao_id int4 NOT NULL,
	ano_inscricao_id int4 NOT NULL,
	data_situacao_id int4 NOT NULL,
	data_cadastramento_id int4 NOT NULL,
	cod_fase_cobranca varchar NOT NULL,
	valor_saldo numeric(15, 2) NOT NULL,
	CONSTRAINT fact_cdas_pkey PRIMARY KEY (id),
	CONSTRAINT fact_cdas_ano_inscricao_id_fkey FOREIGN KEY (ano_inscricao_id) REFERENCES dim_datas(id),
	CONSTRAINT fact_cdas_data_cadastramento_id_fkey FOREIGN KEY (data_cadastramento_id) REFERENCES dim_datas(id),
	CONSTRAINT fact_cdas_data_situacao_id_fkey FOREIGN KEY (data_situacao_id) REFERENCES dim_datas(id),
	CONSTRAINT fact_cdas_natureza_id_fkey FOREIGN KEY (natureza_id) REFERENCES dim_natureza_dividas(id),
	CONSTRAINT fact_cdas_situacao_id_fkey FOREIGN KEY (situacao_id) REFERENCES dim_situacao_cdas(id)
);


-- public.fact_cdas_pessoas definição

-- Drop table

-- DROP TABLE fact_cdas_pessoas;

CREATE TABLE fact_cdas_pessoas (
	id serial4 NOT NULL,
	cda_id int4 NOT NULL,
	pessoa_id int4 NOT NULL,
	sitacao_devedor varchar NOT NULL,
	CONSTRAINT fact_cdas_pessoas_pkey PRIMARY KEY (id),
	CONSTRAINT fact_cdas_pessoas_cda_id_fkey FOREIGN KEY (cda_id) REFERENCES fact_cdas(id),
	CONSTRAINT fact_cdas_pessoas_pessoa_id_fkey FOREIGN KEY (pessoa_id) REFERENCES dim_pessoas(id)
);


-- public.fact_recuperacoes definição

-- Drop table

-- DROP TABLE fact_recuperacoes;

CREATE TABLE fact_recuperacoes (
	id serial4 NOT NULL,
	num_cda varchar NOT NULL,
	prob_recuperacao float8 NOT NULL,
	sts_recuperacao varchar NOT NULL,
	cda_id int4 NOT NULL,
	CONSTRAINT fact_recuperacoes_pkey PRIMARY KEY (id),
	CONSTRAINT fact_recuperacoes_cda_id_fkey FOREIGN KEY (cda_id) REFERENCES fact_cdas(id)
);