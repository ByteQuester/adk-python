import pytest
from starlette.testclient import TestClient
from google.adk.cli.fast_api import get_fast_api_app

@pytest.fixture
def client():
    app = get_fast_api_app(
        agents_dir="/home/mpo/adk/marketing-agency",
        web=True,
    )
    return TestClient(app)

def test_list_agents(client):
    response = client.get("/api/agents")
    assert response.status_code == 200
    assert response.json() == ["marketing_coordinator"]
