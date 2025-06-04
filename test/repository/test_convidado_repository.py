import pytest
from sqlalchemy.exc import IntegrityError

from model import Convidado


class TestConvidadoRepository:
    def test_get_all(self, convidado_repository):
        convidados = convidado_repository.get_all()
        assert len(convidados) == 10

    def test_get_by_id_when_convidado_id_exists_then_return_convidado(self, convidado_repository):
        convidado = convidado_repository.get_by_id(1)
        assert convidado.nome == 'Alice Silva'

    def test_get_by_id_when_convidado_id_does_not_exist_then_return_none(self, convidado_repository):
        convidado = convidado_repository.get_by_id(11)
        assert convidado is None

    def test_get_by_nome_when_convidado_nome_exists_then_return_convidado(self, convidado_repository):
        convidado = convidado_repository.get_by_nome('Bruno Costa')
        assert convidado.nome == 'Bruno Costa'

    def test_get_by_nome_when_convidado_nome_does_not_exist_then_return_none(self, convidado_repository):
        convidado = convidado_repository.get_by_nome('Nao existente')
        assert convidado is None

    def test_get_confirmados(self, convidado_repository):
        convidados = convidado_repository.get_confirmados()
        assert len(convidados) == 4

    def test_get_nao_confirmados(self, convidado_repository):
        convidados = convidado_repository.get_nao_confirmados()
        assert len(convidados) == 3

    def test_get_nao_vai(self, convidado_repository):
        convidados = convidado_repository.get_nao_vai()
        assert len(convidados) == 3

    def test_save_convidado_when_convidado_is_valid_then_save_convidado(self, convidado_repository, convidado_nao_confirmado):
        convidado_repository.save(convidado_nao_confirmado)
        convidado = convidado_repository.get_by_id(11)
        assert convidado.nome == convidado_nao_confirmado.nome

    def test_save_convidado_when_convidado_is_invalid_then_raise_exception(self, convidado_repository):
        convidado = Convidado()
        with pytest.raises(Exception):
            convidado_repository.save(convidado)

    def test_save_convidado_when_convidado_already_exists_then_raise_exception(self, convidado_repository, convidado_nao_confirmado):
        with pytest.raises(IntegrityError):
            convidado_repository.save(convidado_nao_confirmado)

    def test_delete_by_id_when_convidado_exists_then_delete_user(self, convidado_repository, convidado_nao_confirmado):
        convidado_repository.delete_by_id(convidado_nao_confirmado.convidado_id)
        print(convidado_repository.get_by_id(convidado_nao_confirmado.convidado_id))

    def test_delete_by_id_when_convidado_does_not_exist_then_raise_exception(self, convidado_repository):
        with pytest.raises(Exception):
            convidado_repository.delete_by_id(11)

    def test_update_by_id_when_convidado_exists_and_send_name_to_update_then_update_convidado(self, convidado_repository):
        convidado = Convidado()
        convidado.nome = "Joao Paulo"
        convidado_repository.update_by_id(1, convidado)
        convidado = convidado_repository.get_by_id(1)
        assert convidado.nome == "Joao Paulo"

    def test_update_by_id_when_convidado_exists_and_send_presenca_to_update_then_update_convidado(self, convidado_repository):
        convidado = Convidado()
        convidado.presenca = 'nao_confirmado'
        convidado_repository.update_by_id(1, convidado)
        convidado = convidado_repository.get_by_id(1)
        assert convidado.presenca == 'nao_confirmado'
