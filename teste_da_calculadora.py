"""
Teste unitários para a calculadora
"""

import calculadora

class Testando_calculadora:

    def teste_de_soma(self):
        assert 4 == calculadora.somar(2, 2)


    def teste_de_subtracao(self):
        assert 2 == calculadora.subtrair(4, 2)