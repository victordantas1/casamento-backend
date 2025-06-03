import pytest

from model import Convidado

@pytest.fixture
def convidado_nao_confirmado():
    convidado = Convidado()
    convidado.nome = 'Carlos'
    return convidado

@pytest.fixture
def convidado_confirmado():
    convidado = Convidado()
    convidado.nome = 'Luis'
    convidado.presenca_confirmada = True
    return convidado