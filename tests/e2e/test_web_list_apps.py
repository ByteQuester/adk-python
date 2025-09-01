import pytest
from starlette.testclient import TestClient
from google.adk.cli.fast_api import get_fast_api_app

@pytest.fixture
def client():
    app = get_fast_api_app(
        agents_dir="/home/mpo/adk/marketing-agency",
        web_assets_dir="/home/mpo/adk/adk-python/src/google/adk/cli/browser",
        a2a=False,
        host="127.0.0.1",
        port=8000,
        trace_to_cloud=False,
        reload_agents=False,
        web=True,  # keeps default mounting behavior if no custom dir provided
    )
    return TestClient(app)

def test_list_apps(client):
    resp = client.get("/list-apps")
    assert resp.status_code == 200
    assert "marketing_agency" in resp.json()

def test_static_ui_root_redirects(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.url.path == "/dev-ui/"