from dataclasses import dataclass # Import data class 

@dataclass                      # allows you to shorten code rather then using __init__
class Student:
	name: str
	school_id: str
	gpa: float

    def __str__(self):                                  # A function in a class is a method
        return f'Name: {self.name}, GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'abcdef', 3.5)
    
    katie = Student('Katie', 'iadkic', 3.7)
    
    print(alex)
    
    print(katie)

main()
