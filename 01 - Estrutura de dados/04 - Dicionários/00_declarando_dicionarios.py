pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
pessoa["profissão"] = "Eng. Agrimensor "  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(pessoa)
