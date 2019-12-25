from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

beni = Usuario("Beni")
daniel = Usuario("Daniel")
bruno = Usuario("Bruno")

lance_do_bruno = Lance(bruno, 90.00)
lance_do_beni = Lance(beni, 140.00)
lance_do_daniel = Lance(daniel, 150.00)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_bruno)
leilao.lances.append(lance_do_beni)
leilao.lances.append(lance_do_daniel)

for lance in leilao.lances:
    print (f'O usuário {lance.usuario.nome} deu o lance de R$ {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'O menor lance foi de R$ {avaliador.menor_lance} e o maior lance foi de R${avaliador.maior_lance}')
