import unittest
from name_function import get_formatted_name

#testes para name_function.py

class NameTestCase(unittest.TestCase):
    #qualquer método da classe inciado com test_ será executado automaticamente
    def test_first_last_name(self): 
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('vinicius','silva','oliveira')
        self.assertEqual(formatted_name, 'Vinicius Oliveira Silva')

#executa todos os métodos iniciados com test_
unittest.main()