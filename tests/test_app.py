import pytest
from colorama.ansi import clear_line


# 1 homepage( ar atsidaro ) - routas  "/"
def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Projektų lentelė" in response.text


# 2 projekto pridėjimas( ar įsiveda ir išsisaugo
# naujas projektas) - routas "/new"
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


# projekto redagavimas - routas "/projektai/update/<id>"
def test_update_entry(client):
    # formos duomenys, sukuriamas vienoks projektas
    test_data = {"pavadinimas": "Testinisupdate projektas",
                 "plotas": 888,
                 "kaina": 8000
                 }
    response = client.post("/new", data=test_data, follow_redirects=True)
    assert response.status_code == 200
    # assert "Testinisupdate projektas" in response.text

    # updeitinamas projektas su id 1
    test_update_data = {"pavadinimas": "Testinisupdate2 projektas2",
                        "plotas": 700,
                        "kaina": 7777
                        }
    response = client.post("/projektai/update/1", data=test_update_data, follow_redirects=True)
    # tikrinama ar suveikė updeitas
    assert response.status_code == 200
    assert "Testinisupdate2 projektas2" in response.text and "7777" in response.text
    assert "Testinisupdate projektas" not in response.text

# projekto trynimas - routas "/projektai/delete/"
def test_delete_entry(client):
    # formos duomenys, sukuriamas vienoks projektas
    test_data = {"pavadinimas": "Deletetesto projektas",
                 "plotas": 888,
                 "kaina": 8000
                 }
    response = client.post("/new", data=test_data, follow_redirects=True)
    assert response.status_code == 200

    response = client.post("/projektai/delete/1", follow_redirects=True)
    assert response.status_code == 200
    assert "Deletetesto projektas" not in response.text
