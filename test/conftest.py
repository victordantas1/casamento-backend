import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from model import Convidado, PresencaEnum
from repository.convidado_repository import ConvidadoRepository

config_test = {
    'db_url': 'localhost:3307/casamento',
    'db_username': 'victor',
    'db_password': 'senha123',
}

@pytest.fixture
def convidado_nao_confirmado():
    convidado = Convidado(convidado_id=1, nome='Carlos', presenca=PresencaEnum.NAO_CONFIRMADO)
    return convidado

@pytest.fixture
def convidado_confirmado():
    convidado = Convidado()
    convidado.nome = 'Luis'
    convidado.presenca = PresencaEnum.VAI
    return convidado

@pytest.fixture
def database_session():
    return Session(create_engine(f"mysql+pymysql://{config_test['db_username']}:{config_test['db_password']}@{config_test['db_url']}"))

@pytest.fixture
def convidado_repository(database_session):
    return ConvidadoRepository(database_session)