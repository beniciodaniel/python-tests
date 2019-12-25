from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_deve_retornar_o_maior_e_o_menor_numero_quando_adicionados_em_ordem_crescente(self):
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


    def test_deve_retornar_o_maior_e_o_menor_numero_quando_adicionados_em_ordem_decrescente(self):
        beni = Usuario("Beni")
        daniel = Usuario("Daniel")

        lance_do_daniel = Lance(daniel, 150.00)
        lance_do_beni = Lance(beni, 100.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_beni)
        leilao.lances.append(lance_do_daniel)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_quando_tiver_somente_um_lance(self):
        beni = Usuario("Beni")

        lance = Lance(beni, 150.0)

        leilao = Leilao("Celular")
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150, avaliador.menor_lance)
        self.assertEqual(150, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_tiver_tres_lances(self):
        bruno = Usuario("Bruno")
        beni = Usuario("Beni")
        daniel = Usuario("Daniel")

        lance_do_bruno = Lance(bruno, 90.0)
        lance_do_beni = Lance(beni, 140.0)
        lance_do_daniel = Lance(daniel, 150.0)

        leilao = Leilao("Celular")

        leilao.lances.append(lance_do_bruno)
        leilao.lances.append(lance_do_daniel)
        leilao.lances.append(lance_do_beni)

        menor_valor_esperado = 90.0
        maior_valor_esperado = 150.0

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)