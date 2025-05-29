USE casamento;

CREATE TABLE convidado (
    convidado_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    presenca_confirmada BOOLEAN NOT NULL
);

CREATE TABLE noivo (
    noivo_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);