import unittest

from survey import AnonymousSurvey

#teste para classe AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    #cria uma pesquisa e um conjunto de resposta para utilizar em todos os testes da classe
    def setUp(self):
        question = "What language did you first learned?"
        self.my_survey = AnonymousSurvey(question)       
        self.responses = ['English', 'Portuguese', 'French']

    def test_storeSingleResponse(self):
        self.my_survey.storeResponse(self.responses[0])
        #verifica se o primeiro parâmetro esta armazenado no segundo
        self.assertIn('English', self.my_survey.responses)

    def test_storeThreeResponses(self):
        for r in self.responses:
            self.my_survey.storeResponse(r)

        for r in self.responses:
            self.assertIn(r,self.my_survey.responses)
    

unittest.main()