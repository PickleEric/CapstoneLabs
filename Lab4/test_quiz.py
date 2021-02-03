import quiz
import unittest
from unittest import TestCase

class TestQuiz(TestCase):

    def test_quiz_with_string_answers(self):

        right_answer = 'Madison'
        user_answer = 'Madison'

        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)
    def test_quiz_different_cases(self):
        right_answer = 'Madison'
        uswer_answer = 'MADISON'

        result = quiz.is_correct_answer(right_answer, uswer_answer)
        self.assertTrue(result)

    def test_quiz_reports_wrong_answer(self):
        right_answer = 'Madison'
        user_answer = "Saint Paul"

        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertFalse(result)

    def test_quiz_numeric_answers(self):
        right_answer = 42
        user_answer = 42

        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)

    def test_quiz_numeric_answer_wrong_answer(self):
        right_answer = 200
        user_answer = 150
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertFalse(result)
        
    def test_quiz_numeric_and_string_answer_right(self):
        right_answer = 100
        user_answer = '100'
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()