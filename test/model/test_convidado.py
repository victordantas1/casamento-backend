import pytest

from model import Convidado


class TestConvidado:
    def test_confirma_presenca_when_presenca_nao_confirmada_then_confirme(self, convidado_nao_confirmado):
        # Act
        convidado_nao_confirmado.confirma_presenca()

        # Assert
        assert convidado_nao_confirmado.presenca_confirmada == True

    def test_confirma_presenca_when_presenca_ja_confirmada_then_raise_exception(self, convidado_confirmado):
        with pytest.raises(Exception, match='Presença já confirmada'): # Assert
            convidado_confirmado.confirma_presenca() # Act

    def test_desconfirma_presenca_when_presenca_ja_confirmada_then_desconfirme(self, convidado_confirmado):
        # Act
        convidado_confirmado.desconfirma_presenca()

        # Assert
        assert convidado_confirmado.presenca_confirmada == False

    def test_desconfirma_presenca_when_presenca_nao_confirmada_then_raise_exception(self, convidado_nao_confirmado):
        with pytest.raises(Exception, match='Presença ainda não confirmada'): # Assert
            convidado_nao_confirmado.desconfirma_presenca() # Act

    def test_atualiza_campos_when_convidado_nao_vazio_then_atualiza_campos(self, convidado_confirmado):
        # Arrange
        convidado = Convidado()
        convidado.nome = 'Roberto'
        convidado.presenca_confirmada = False

        # Act
        convidado_confirmado.atualiza_campos(convidado)

        # Assert
        assert convidado_confirmado.nome == 'Roberto'
        assert convidado_confirmado.presenca_confirmada == False

    def test_atualiza_campos_when_convidado_vazio_then_raise_exception(self, convidado_confirmado):
        # Arrange
        convidado = Convidado()

        with pytest.raises(Exception, match='Campos vazios'): # Act
            convidado.atualiza_campos(convidado) # Assert