import unittest

from survey import AnonymousSurvey

#teste para classe AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def test_storeSingleResponse(self):
        question = "What language did you first learned?"
        my_survey = AnonymousSurvey(question)
        my_survey.storeResponse('English')
        #verifica se o primeiro parâmetro esta armazenado no segundo
        self.assertIn('English', my_survey.responses)

    def test_storeThreeResponses(self):
        question = "What language did you first learned?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Portuguese', 'French']
        for r in responses:
            my_survey.storeResponse(r)

        for r in responses:
            self.assertIn(r,my_survey.responses)
    

unittest.main()