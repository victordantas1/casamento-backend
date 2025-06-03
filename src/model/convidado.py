from sqlalchemy import Column, Integer, String, Enum

from db import Base

class Convidado(Base):
    __tablename__ = 'convidado'

    convidado_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    presenca = Column(Enum, nullable=False, default='nao_confirmado')

    def confirma_presenca(self):
        if self.presenca:
            raise Exception('Presença já confirmada')
        self.presenca = True

    def desconfirma_presenca(self):
        if self.presenca:
            self.presenca = False
        else:
            raise Exception('Presença ainda não confirmada')

    def atualiza_campos(self, convidado):
        if convidado.nome and convidado.presenca is not None:
            self.nome = convidado.nome
            self.presenca = convidado.presenca
        else:
            raise Exception('Campos vazios')