from src.leilao.dominio import Usuario, Lance, Leilao

beni = Usuario("Beni")
daniel = Usuario("Daniel")
bruno = Usuario("Bruno")

lance_do_bruno = Lance(bruno, 90.00)
lance_do_beni = Lance(beni, 140.00)
lance_do_daniel = Lance(daniel, 150.00)

leilao = Leilao("Celular")

leilao.propoe(lance_do_bruno)
leilao.propoe(lance_do_beni)
leilao.propoe(lance_do_daniel)

for lance in leilao.lances:
    print (f'O usuário {lance.usuario.nome} deu o lance de R$ {lance.valor}')



print(f'O menor lance foi de R$ {leilao.menor_lance} e o maior lance foi de R${leilao.maior_lance}')
