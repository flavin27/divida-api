# Avisos sobre o repositório

Esse repositório consiste em um teste para uma vaga de inciação científica e por isso todo o projeto sera anonimizado para preservar a realização do teste.


## Sobre

API que permite consultas de dados referentes a dívida pública provenientes de um data warehouse. A API é construída utilizando o framework FastAPI para fornercer endpoints RESTful.

## Arquitetura

### Parsers
Responsavéis por converter os dados brutos vindos dos csvs para um array de DTO

### DTOs

Objetos para encapsular os dados em um formato fixo com validações previamente definidas. Esses dados são transformados quando recebidos de uma fonte externa, seja ela um arquivo de terceiros, como o caso dos csv, ou uma requisiçao no servidor no formato de Request.

### Repositories

Camada de abstração para isolar a logica referente a persistência dos dados.

### Migrations

Automação da criação de tabelas por meio de scripts em alto nível integrados ao sistema


### Seeders

Camada responsável por popular o banco de dados e o data warehouse

## Como rodar

1 - Clone o repositório

```bash
$ git clone https://github.com/PedroZborowski/projeto-lamdec
$ cd projeto-lamdec
```

2 - Adicione a raiz do projeto a pasta /data contendo os arquivos csv que serão utilizados como data set.

3 - Compile a imagem do docker

```bash
docker-compose build
docker-compose run --rm migrate
docker-compose run --rm seed
docker-compose run --rm test
docker-compose up api
```

4 - Acesse a documentação

Acesse o url para verificar em qualquer navegador
```bash
http://localhost:8000/docs
```

## Aviso Legal

Este repositório contém o código desenvolvido como parte de um teste técnico proposto pelo laboratório responsável pela vaga de iniciação científica.

Todos os direitos sobre o código, dados e materiais relacionados pertencem exclusivamente ao laboratório proponente do teste.

O uso, distribuição ou modificação deste repositório deve respeitar as políticas e termos definidos pelo laboratório, não sendo permitida a utilização fora do contexto do processo seletivo sem autorização expressa.

O propósito deste repositório é exclusivamente para avaliação técnica e acadêmica vinculada à vaga em questão.