from enum import Enum


class PresencaEnum(str, Enum):
    VAI = 'vai'
    NAO_CONFIRMADO = 'nao_confirmado'
    NAO_VAI = 'nao_vai'