
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def test(self):
        question = 'what language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)

        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)
    def test_three_responses(self):
        question = 'what language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['ddkv','sdvk','svj','sjav']
        for n in responses:
            my_survey.store_response(n)
        for i in responses:
            self.assertIn(i, my_survey.responses)


'''if __name__=="__main__":
    unittest.main()'''

