#!/usr/bin/env python

from user import User
# 4. We've given you a barebones `Student` class. Change the class definition so
#    that it inherits from the `User` class. Run the test suite and notice that
#    you are passing some tests for the `Student` class, even without writing any
#    code inside that class. That is because it will inherit the `first_name` and
#    `last_name` attributes from the `User` class you told it to inherit from.
class Student(User):
   
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        
    def learn(self, skills):
        self.knowledge.append(skills)