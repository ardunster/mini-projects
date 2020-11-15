from eightkeys.common.functions import ni, ne, si, se, ti, te, fi, fe


class Question:
    """
    Basic question class
    """
    def __init__(self, text, function, target, value):
        self.text = text
        self.function = function
        self.target = target
        self.options = []
        if self.target == "preference":
            self.text += "\nRank from 1 (Not like me) to 5 (A lot like me)."
            self.value = 1
            self.options = [1, 2, 3, 4, 5]
        elif self.target == "development":
            self.text += "\nSelect from 1: no, 2: a little/sometimes, 3: yes."
            self.value = value
            self.options = [1, 2, 3]

    # Gets and validates input
    def get_input(self):
        user_input = ''
        error = "Invalid selection, please select from [ "
        error += ', '.join(str(x) for x in self.options) + " ]"
        while user_input == '':
            user_input = input()
            if user_input.isdigit():
                if int(user_input) in self.options:
                    return int(user_input)
                else:
                    print(error)
                    user_input = ''
            else:
                print(error)
                user_input = ''

    # Asks the question, stores the validated input in a variable
    def ask(self):
        print(self.text)
        self.answer = self.get_input()

    # Converts the stored validated input into a score, and
    # adds it to the function
    def score(self):
        if self.target == "preference":
            if self.answer == 1:
                score = -2
            elif self.answer == 2:
                score = -1
            elif self.answer == 3:
                score = 0
            elif self.answer == 4:
                score = 1
            elif self.answer == 5:
                score = 2
            self.function.preference += score
        elif self.target == "development":
            if self.answer == 1:
                score = 0
            elif self.answer == 2:
                score = (self.value * 0.5)
            elif self.answer == 3:
                score = self.value
            self.function.development += score


preference_questions = [
    Question("Red?", ni, "preference", 3),
    Question("Stevesicle?", se, "development", 20)
]
