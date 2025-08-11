import pytest
from unittest.mock import patch, MagicMock
from App.Http.Controllers.CdaController import CdaController


@pytest.fixture
def mock_repository():
    repo = MagicMock()
    repo.index.return_value = [{"num_cda": "123", "valor": 1000}]
    repo.get_distribuicao_cdas.return_value = [{"natureza": "Imposto", "total": 5}]
    return repo


def test_index(mock_repository):
    with patch("App.Http.Controllers.CdaController.SessionLocal", return_value="fake_session"), \
        patch("App.Http.Controllers.CdaController.FactCdaRepository", return_value=mock_repository):

        response = CdaController.index(request="fake_request")

        assert response["status"] == "ok"
        assert isinstance(response["data"], list)
        assert response["data"][0]["num_cda"] == "123"


def test_index_distribuicao_cda(mock_repository):
    with patch("App.Http.Controllers.CdaController.SessionLocal", return_value="fake_session"), \
        patch("App.Http.Controllers.CdaController.FactCdaRepository", return_value=mock_repository):

        response = CdaController.index_distribuicao_cda()

        assert response["status"] == "ok"
        assert response["data"][0]["natureza"] == "Imposto"
