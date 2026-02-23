import pytest

# 1 homepage( ar atsidaro ) - routas  "/"
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Projektų lentelė" in response.text

# 2 projekto pridėjimas( ar įsiveda ir išsisaugo
# naujas projektas) - routas "/ne"w"
def test_add_entry(client):
    # formos duomenys
    test_data = {"pavadinimas": "Testinis projektas",
                 "plotas": 888,
                 "kaina": 8000
    }
    response = client.post("/new", data=test_data, follow_redirects=True)

    # ar linkas ir postas suveikė
    assert response.status_code == 200
    # ar po redirekto(į homepage), atsirado duomenys su tekstu "Testinis projektas"
    assert "Testinis projektas" in response.text and "888" in response.text
