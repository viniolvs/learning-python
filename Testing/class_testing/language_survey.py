from survey import AnonymousSurvey

#define pergunta e cria pesquisa
question = "What language did you first learned?"

my_survey = AnonymousSurvey(question)
my_survey.showQuestion()
print("Enter q to quit\n")

while True:
    response = input("Answer: ")
    if response == 'q':
        break
    my_survey.storeResponse(response)

my_survey.showResults()