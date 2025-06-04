from typing import Optional, List

from sqlalchemy import select
from sqlalchemy.orm import Session

from model import Convidado


class ConvidadoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, convidado_id: int) -> Optional[Convidado]:
        return self.session.get(Convidado, convidado_id)

    def get_all(self) -> List[Convidado]:
        stmt = select(Convidado)
        result = self.session.execute(stmt)
        convidados = result.scalars().all()
        return list(convidados)

    def get_by_nome(self, nome: str) -> Optional[Convidado]:
        stmt = select(Convidado).where(Convidado.nome == nome)
        result = self.session.execute(stmt)
        convidado = result.scalar()
        return convidado

    def get_confirmados(self) -> List[Convidado]:
        stmt = select(Convidado).where(Convidado.presenca == 'vai')
        result = self.session.execute(stmt)
        convidados = result.scalars().all()
        return list(convidados)

    def get_nao_confirmados(self) -> List[Convidado]:
        stmt = select(Convidado).where(Convidado.presenca == 'nao_confirmado')
        result = self.session.execute(stmt)
        convidados = result.scalars().all()
        return list(convidados)

    def get_nao_vai(self):
        stmt = select(Convidado).where(Convidado.presenca == 'nao_vai')
        result = self.session.execute(stmt)
        convidados = result.scalars().all()
        return list(convidados)

    def save(self, convidado: Convidado) -> Convidado:
        try:
            self.session.add(convidado)
            self.session.commit()
            return convidado
        except:
            self.session.rollback()
            raise

    def delete_by_id(self, convidado_id: int) -> Optional[Convidado]:
        try:
            convidado = self.get_by_id(convidado_id)
            self.session.delete(convidado)
            self.session.commit()
            return convidado
        except:
            self.session.rollback()
            raise

    def update_by_id(self, convidado_id: int, convidado: Convidado) -> Convidado:
        try:
            convidado_to_update = self.get_by_id(convidado_id)
            convidado_to_update.atualiza_campos(convidado)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return convidado_to_update