import unittest
from calculadora import somar, subtrair, multiplicar, dividir, porcentagem

class TestCalculadora(unittest.TestCase):
    
    # --- Testes de Soma ---
    def test_soma_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)
        
    def test_soma_com_negativos(self):
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-5, -5), -10)
        
    def test_soma_com_decimais(self):
        self.assertAlmostEqual(somar(1.5, 2.5), 4.0)

    # --- Testes de Subtração ---
    def test_subtracao_positivos(self):
        self.assertEqual(subtrair(10, 4), 6)
        
    def test_subtracao_resultado_negativo(self):
        self.assertEqual(subtrair(3, 7), -4)

    # --- Testes de Multiplicação ---
    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicar(3, 5), 15)
        
    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicar(10, 0), 0)
        
    def test_multiplicacao_com_negativo(self):
        self.assertEqual(multiplicar(4, -2), -8)

    # --- Testes de Divisão ---
    def test_divisao_exata(self):
        self.assertEqual(dividir(10, 2), 5.0)
        
    def test_divisao_com_decimal(self):
        self.assertAlmostEqual(dividir(5, 2), 2.5)
        
    def test_divisao_por_zero(self):
        self.assertEqual(dividir(10, 0), "Erro: Não é possível dividir por zero!")

    # --- Testes de Porcentagem ---
    def test_porcentagem_padrao(self):
        # 15% de 200 = 30
        self.assertEqual(porcentagem(200, 15), 30.0)
        
    def test_porcentagem_cem_porcento(self):
        # 100% de 50 = 50
        self.assertEqual(porcentagem(50, 100), 50.0)
        
    def test_porcentagem_zero_porcento(self):
        # 0% de 80 = 0
        self.assertEqual(porcentagem(80, 0), 0.0)

if __name__ == "__main__":
    unittest.main()
