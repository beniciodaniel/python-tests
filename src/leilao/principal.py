from src.leilao.dominio import Usuario, Lance, Leilao

beni = Usuario("Beni")
daniel = Usuario("Daniel")

lance_do_beni = Lance(beni, 100.0)
lance_do_daniel = Lance(daniel, 150.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_beni)
leilao.lances.append(lance_do_daniel)

for lance in leilao.lances:
    print (f'O usuário {lance.usuario.nome} deu o lance de R$ {lance.valor}')