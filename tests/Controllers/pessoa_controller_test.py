import pytest
from unittest.mock import patch, MagicMock
from App.Http.Controllers.PessoaController import PessoaController


@pytest.fixture
def mock_repository():
    mock_repo = MagicMock()
    # Simulando a lista de DTOs retornados pelo repository
    mock_repo.index.return_value = [
        MagicMock(nome="João Silva", tipo_documento="CPF", documento="123.456.789-00"),
        MagicMock(nome="Empresa X", tipo_documento="CNPJ", documento="12.345.678/0001-99")
    ]
    return mock_repo


def test_pessoa_index(mock_repository):
    with patch("App.Http.Controllers.PessoaController.SessionLocal") as mock_session, \
        patch("App.Http.Controllers.PessoaController.DimPessoaRepository", return_value=mock_repository):

        mock_session_instance = MagicMock()
        mock_session.return_value = mock_session_instance

        response = PessoaController.index()

        # Testa o status da resposta
        assert response["status"] == "ok"

        # Testa o formato dos dados retornados
        data = response["data"]
        assert isinstance(data, list)
        assert data[0]["name"] == "João Silva"
        assert data[0]["tipo_pessoa"] == "CPF"
        assert data[0]["CPF/CNPJ"] == "123.456.789-00"

        # Confirma que a sessão foi fechada
        mock_session_instance.close.assert_called_once()
