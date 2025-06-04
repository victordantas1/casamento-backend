from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import Mapped

from db import Base
from model.presenca_enum import PresencaEnum


class Convidado(Base):
    __tablename__ = 'convidado'

    convidado_id: Mapped[int] = Column(Integer, primary_key=True)
    nome: Mapped[str] = Column(String, nullable=False)
    presenca: Mapped[PresencaEnum] = Column(Enum, nullable=False, default='nao_confirmado')

    def confirma_presenca(self):
        if self.presenca.value == 'vai':
            raise Exception('Presença já confirmada')
        self.presenca = PresencaEnum.VAI

    def desconfirma_presenca(self):
        if self.presenca.value == 'vai':
            self.presenca = PresencaEnum.NAO_CONFIRMADO
        else:
            raise Exception('Presença ainda não confirmada')

    def atualiza_campos(self, convidado):
        if convidado.nome and convidado.presenca is not None:
            self.nome = convidado.nome
            self.presenca = convidado.presenca
        else:
            raise Exception('Campos vazios')