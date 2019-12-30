from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao

class TestAvaliador(TestCase):

    def setUp(self):
        self.beni = Usuario("Beni")
        self.lance_do_beni = Lance(self.beni, 100.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_numero_quando_adicionados_em_ordem_crescente(self):
        daniel = Usuario("Daniel")
        lance_do_daniel = Lance(daniel, 150.00)

        self.leilao.propoe(self.lance_do_beni)
        self.leilao.propoe(lance_do_daniel)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_numero_quando_adicionados_em_ordem_decrescente(self):

        self.leilao.propoe(self.lance_do_beni)
        self.daniel = Usuario("Daniel")
        self.lance_do_daniel = Lance(self.daniel, 150.00)
        self.leilao.propoe(self.lance_do_daniel)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_quando_tiver_somente_um_lance(self):
        lance = Lance(self.beni, 150.0)

        self.leilao.propoe(lance)

        self.assertEqual(150, self.leilao.menor_lance)
        self.assertEqual(150, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_tiver_tres_lances(self):
        daniel = Usuario("Daniel")

        bruno = Usuario("Bruno")

        lance_do_bruno = Lance(bruno, 90.0)
        lance_do_daniel = Lance(daniel, 150.0)
        lance_do_beni = Lance(self.beni, 140.0)

        self.leilao.propoe(lance_do_bruno)
        self.leilao.propoe(lance_do_daniel)
        self.leilao.propoe(lance_do_beni)

        menor_valor_esperado = 90.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
