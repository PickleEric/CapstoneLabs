import camelCase
from unittest import TestCase
"""
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
"""
class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))

    def test_a_single_word_used(self):
        bad_string = 'word'

        result = camelCase.camel_case(bad_string)

        self.assertFalse(result)

    def test_if_left_blank(self):
        bad_string = ''

        result = camelCase.camel_case(bad_string)

        self.assertTrue(result)
