from sqlalchemy import Column, Integer, String, Boolean

from db import Base

class Convidado(Base):
    __tablename__ = 'convidado'

    convidado_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    presenca_confirmada = Column(Boolean, nullable=False, default=False)

    def confirma_presenca(self):
        self.presenca_confirmada = True

    def atualiza_campos(self, convidado):
        self.nome = convidado.nome
        self.presenca_confirmada = convidado.presenca_confirmada
