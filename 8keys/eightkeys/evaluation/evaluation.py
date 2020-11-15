# from eightkeys.common.cfunctions import ni, ne, si, se, ti, te, fi, fe
from eightkeys.evaluation.questions import preferences, development


class Question:
    """
    Basic question class
    """
    def __init__(self, text, cfunction, target, value=1):
        self.text = text
        self.cfunction = cfunction
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
            self.cfunction.preference += score
            self.cfunction.total_pref += 2
        elif self.target == "development":
            if self.answer == 1:
                score = 0
            elif self.answer == 2:
                score = (self.value * 0.5)
            elif self.answer == 3:
                score = self.value
            self.cfunction.development += score
            self.cfunction.total_dev += self.value


def make_preference_questions():
    preference_questions = []

    for i, line in enumerate(preferences):
        text = (preferences[i][0] + "\n" + preferences[i][1])
        preference_questions.append(
            Question(text, preferences[i][2], "preference")
            )

    return preference_questions


def make_development_questions():
    development_questions = []

    for i, line in enumerate(development):
        text = development[i][0]
        cfunc = development[i][1]
        value = development[i][2]
        development_questions.append(
            Question(text, cfunc, "development", value)
            )
