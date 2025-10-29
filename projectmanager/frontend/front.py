import requests

BASE_URL = 'http://localhost:8000/api/'

def cadastrar():
    username = input("Usuário: ")
    password = input("Senha: ")
    data = {"username": username, "password": password}
    response = requests.post(BASE_URL + "usuarios/", json=data)

    if response.status_code == 201:
        print("Usuário criado com sucesso!")
    else:
        print("Erro ao cadastrar:", response.text)


    
