'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''
import unittest
from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_who_is_not_in_the_list_raises_student_error(self):
        test_class = ClassList(4)
        test_class.add_student('Alice')
        test_class.add_student('Larry')
         # remove "carl'", expect a StudentError
         # action and assert together
        with self.assertRaises(StudentError):
            # action
            test_class.remove_student('Carl')

    ## TODO write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list_show_error(self):
        test_class = ClassList(1)  # ClassList should allow at least one student

        with self.assertRaises(StudentError):
            test_class.remove_student('Jim')


    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.
    def test_student_not_in_class_is_not_entrolled(self):
        test_class = ClassList(4)
        test_class.add_student('Alice')
        test_class.add_student('Bob')
        is_carl_enrolled = test_class.is_enrolled('Carl')
        self.assertFalse(is_carl_enrolled)

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_if_class_list_is_empty(self):
        test_class = ClassList(1)  # at least one student
        self.assertIsNone(test_class.index_of_student(0))
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_who_is_not_in_class_to_be_none(self):
        test_class = ClassList(2)
        test_class.add_student('Harry')
        test_class.add_student('Sally')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Sally'))

        self.assertIsNone(test_class.index_of_student('Berry'))
   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.
    def test_if_class_is_full_method(self):
        test_class = ClassList(5)
        # add 5 students
        test_class.add_student('a')
        test_class.add_student('b')
        test_class.add_student('c')
        test_class.add_student('d')
        test_class.add_student('e')

        # now expect class to be full
        result = test_class.is_class_full()

        self.assertTrue(result)


    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.
    def test_if_class_is_empty_method(self):
        test_class = ClassList(1)   # shouldn't be allowed to make a class with max 0 students 

        result = test_class.is_class_full()

        self.assertFalse(result)

    def test_if_class_is_zero(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(0)

    def test_if_class_is_negative(self):
        with self.assertRaises(StudentError):
            test_class = ClassList(-1)

if __name__ == '__main__':
    unittest.main()