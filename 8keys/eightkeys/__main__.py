#!/usr/bin/env python3

from eightkeys.common.cfunctions import ni, ne, si, se, ti, te, fi, fe
import eightkeys.evaluation.evaluation as evaluation

cfunctions = [ni, ne, si, se, ti, te, fi, fe]

if __name__ == '__main__':
    prefs = evaluation.make_preference_questions()
    for question in prefs:
        question.ask()
        question.score()
    print("Preference Scores:")
    for cfunc in cfunctions:
        print(cfunc.name + ": " + str(cfunc.preference))

    devs = evaluation.make_development_questions()
    for question in devs:
        question.ask()
        question.score()
    print("Development Scores:")
    for cfunc in cfunctions:
        print(cfunc.name + ": " + str(cfunc.development))
