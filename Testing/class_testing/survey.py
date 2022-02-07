#coleta respostas annonimas para uma pergunta de pesquisa


class AnonymousSurvey():
    def __init__(self,question) -> None:
        self.question = question
        self.responses = []
    
    def showQuestion(self):
        print(self.question)
    
    def storeResponse(self, new_response):
        self.responses.append(new_response)
    
    def showResults(self):
        print("Results: ")
        for response in self.responses:
            print('- ' + response)
