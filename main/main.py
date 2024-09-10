import json

dados = []
print()
print('Faça seu cadastro.')

while True:
    nome = str(input('Nome: '))
    sobrenome = str(input('Sobrenome: '))
    email = str(input('Email: '))
    telefone = input('Telefone: ')
    texto = str(input('CADASTRO REALIZADO! Deseja fazer outro cadastro? sim[s] não[n]: '))
    print()

    class PESSOA:
        def __init__(self, nome, sobrenome, email, telefone) -> None:
            self.nome = nome
            self.sobrenome = sobrenome
            self.email = email
            self.telefone = telefone
    
    p1 = PESSOA(nome, sobrenome, email, telefone)
    
    dados.append(p1.__dict__)
    
    if texto in 'n':
        break

#print(dados)

CAMINHO = 'main\\dados_pessoas.json'

with open(CAMINHO, 'w', encoding='utf8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

