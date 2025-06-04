CREATE DATABASE IF NOT EXISTS casamento;

CREATE TABLE casamento.convidado (
    convidado_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    presenca ENUM('vai', 'nao_confirmado', 'nao_vai') NOT NULL DEFAULT 'nao_confirmado'
);

CREATE TABLE casamento.noivo (
    noivo_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

INSERT INTO casamento.convidado (convidado_id, nome, presenca) VALUES
    (1, 'Alice Silva', 'vai'),
    (2, 'Bruno Costa', 'nao_confirmado'),
    (3, 'Carla Santos', 'nao_vai'),
    (4, 'Daniel Pereira', 'vai'),
    (5, 'Eduarda Lima', 'nao_confirmado'),
    (6, 'Felipe Oliveira', 'vai'),
    (7, 'Gabriela Souza', 'nao_vai'),
    (8, 'Henrique Martins', 'nao_confirmado'),
    (9, 'Isabela Ferreira', 'vai'),
    (10, 'João Rodrigues', 'nao_vai');