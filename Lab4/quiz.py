# can you see the bug in this program?

def is_correct_answer(user_answer, correct_answer):
    """ Check if user's answer is the same as the correct
    answer, ignoring case """
    #return str(user_answer).lower() == str(correct_answer).lower()
    string_correct_answer = str(correct_answer).lower()
    string_user_answer = str(user_answer).lower()
    return string_correct_answer == string_user_answer
    #return string_correct_answer == string_correct_answer
    #breaking code that works is a regression

def main():
    question = 'How many senators in the US senate?'
    answer = 100
    
    print(question)
    user_answer = input('What is your answer? ')
    
    if is_correct_answer(user_answer, answer):
        print('Correct!')
    else:
        print(f'Sorry, the answer is {answer}')


if __name__ == '__main__':
    main()