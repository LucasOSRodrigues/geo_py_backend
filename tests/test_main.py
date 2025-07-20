from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# guarda o id do ponto criado para poder deleta-lo
ponto_id = None

def test_adicionar_usuario():
    response = client.post("/AdicionarUsuario/?email=test@gmail.com&nome=test")
    assert response.status_code == 200
    assert "Usuário criado" in response.json()["mensagem"]

def test_adicionar_ponto():
    global ponto_id
    response = client.post("/AdicionarPonto/?latitude=-45.8952&longitude=38.5648&email=test@gmail.com")
    # guarda o id do ponto criado
    ponto_id = response.json()["id"]
    assert response.status_code == 200
    assert "Ponto adicionado" in response.json()["mensagem"]

def test_remover_ponto():
    global ponto_id
    # usa o id para remover o ponto
    response = client.delete(f"/RemoverPonto/?id={ponto_id}&user=test")
    assert response.status_code == 200
    assert "Ponto removido" in response.json()["mensagem"]

def test_remover_usuario():
    response = client.delete("/RemoverUsuario/?email=test@gmail.com")
    assert response.status_code == 200
    assert "Usuário removido" in response.json()["mensagem"]
