#!/usr/bin/env python

from user import User

import random
#    We've given you a barebones `Teacher` class in `lib/teacher.py`. Change the
#    class definition so that the `Teacher` class inherits from the `User` class.
#    Run the test suite and notice that you are passing some tests for the
#    `Teacher` class, even without writing any code inside that class. That is
#    because it will inherit the `first_name` and `last_name` attributes from the
#    `User` class you told it to inherit from. We've given you a list of
#    knowledge strings below; modify the `Teacher` class so that it initializes
#    with this list stored as an attribute, `self.knowledge`.
class Teacher(User):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]