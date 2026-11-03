"""demo-app 的单元测试，Jenkins 流水线的测试阶段会执行它。"""
import os

os.environ.setdefault("APP_VERSION", "test")

from app import app  # noqa: E402


def test_health_ok():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"


def test_index_has_version():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["version"] == "test"
