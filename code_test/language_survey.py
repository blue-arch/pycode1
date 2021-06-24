from survey import AnonymousSurvey

question = 'what language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('enter q to quit at any time:')
while True:
    response = input('Language')
    if response=='q':
        break
    my_survey.store_response(response)


print('thanks for your cooperation')
my_survey.show_results()