#tuplas de convidados
convidados = ("Cauã", "Ana","Manuela", "Alice", "Mauricio", "Deise")
#lista de confirmação
confirmados = ["Cauã", "Ana", "Deise"]
#indicar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
#exibir os convidados que não confirmaram
print("convidados que ainda não confirmaram")
for pessoa in nao_confirmados:
    print(pessoa)
#enviar lembrete para os não confirmados
print("\nEnviar lembrete para não confirmados")