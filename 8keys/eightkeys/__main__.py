#!/usr/bin/env python3

from eightkeys.common.functions import ni, ne, si, se, ti, te, fi, fe
import eightkeys.evaluation.questions as questions

if __name__ == '__main__':
    print(ni.name, ne.name, si.name, se.name, ti.name, te.name, fi.name,
          fe.name)
    print(ni.preference)
    for question in questions.preference_questions:
        question.ask()
        question.score()
    print("Ni: ", ni.preference)
    print("Se: ", se.development)
