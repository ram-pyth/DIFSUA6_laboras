import pytest

# 1 homepage( ar atsidaro )
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Projektų lentelė" in response.text
