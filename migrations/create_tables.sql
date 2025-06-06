CREATE DATABASE IF NOT EXISTS casamento;
USE casamento;

CREATE TABLE convidado (
    convidado_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    presenca ENUM('vai', 'nao_confirmado', 'nao_vai') NOT NULL DEFAULT 'nao_confirmado'
);

CREATE TABLE noivo (
    noivo_id INT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);