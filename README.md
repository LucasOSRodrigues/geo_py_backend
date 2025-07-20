# Backend em Python

Backend em Python com FastAPI para cadastro de usuários e pontos geográficos.

## Estrutura

- `src/`: Código principal
    - `main.py`: Ponto de entrada da aplicação e rotas
    - `models.py`: Modelos de dados
    - `crud.py`: Funções de CRUD para o banco de dados
    - `database.py`: Configuração do banco de dados
- `tests/`: Testes automatizados com PyTest
  - `test_main.py`: Testes para as funções de CRUD

## Como rodar a aplicação
```bash
uvicorn src.main:app --reload --port 8080
```

## Como rodas os testes
``` bash
pytest
```