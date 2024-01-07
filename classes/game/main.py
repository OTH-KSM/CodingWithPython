#!/usr/bin/env python3
from LearnPython.classes.game.Question import question

question_prompts = [
    "What color are strawberries?\n(a) Red\n(b) Blue\n(c) Yellow\n\n",
    "What color are bananas?\n(a) Blue\n(b) Yellow\n(c) Red\n\n",
    "What color are oranges?\n(a) Yellow\n(b) Blue\n(c) Orange\n\n",
]

questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)