from typing import Optional, List
from config import config
from model import Convidado
from repository.convidado_repository import ConvidadoRepository


class ConvidadoService:
    def __init__(self, repository: ConvidadoRepository):
        self.repository = repository

    def get_by_id(self, convidado_id: int) -> Optional[Convidado]:
        convidado = self.repository.get_by_id(convidado_id)
        if convidado is None:
            raise Exception('Convidado nao encontrado')
        else:
            return convidado

    def get_all(self) -> List[Convidado]:
        convidados = self.repository.get_all()
        return convidados

    def get_by_nome(self, nome: str) -> Optional[Convidado]:
        convidado = self.repository.get_by_nome(nome)
        if convidado is None:
            raise Exception('Convidado nao encontrado')

    def get_confirmados(self) -> List[Convidado]:
        convidados = self.repository.get_confirmados()
        return convidados

    def get_nao_confirmados(self) -> List[Convidado]:
        convidados = self.repository.get_nao_confirmados()
        return convidados

    def get_nao_vai(self):
        convidados = self.repository.get_nao_vai()
        return convidados

    def save(self, convidado: Convidado):
        qtd_convidados = len(self.repository.get_all())
        if qtd_convidados > config['convidado_max']:
            raise Exception('Quantidade de convidados maxima atingida')
        else:
            self.repository.save(convidado)

    def delete_by_id(self, convidado_id: int):
        self.repository.delete_by_id(convidado_id)

    def update_by_id(self, convidado_id: int, convidado: Convidado) -> Convidado:
        convidado = self.repository.update_by_id(convidado_id, convidado)
        return convidado

