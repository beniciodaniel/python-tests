from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        beni = Usuario("Beni")
        daniel = Usuario("Daniel")

        lance_do_beni = Lance(beni, 100.0)
        lance_do_daniel = Lance(daniel, 150.00)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_beni)
        leilao.lances.append(lance_do_daniel)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)