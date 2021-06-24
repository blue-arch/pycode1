


class AnonymousSurvey():
    def __init__(self , question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("survey results")
        for n in self.responses:
            print('- '+n)

'''a=AnonymousSurvey('acc')
a.show_question()
a.store_response('a')
a.show_results()'''