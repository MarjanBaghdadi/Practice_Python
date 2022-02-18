#credit: freecodecamp Youtube Channel

from Question import Question

question_prompts = [
    "what color is the sky? \n(a)blue \n(b)yellow \n(c)red\n\n",
    "what color is the grass? \n(a)blue \n(b)yellow \n(c)green\n\n",
    "what color is the cloud? \n(a)blue \n(b)white \n(c)red\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
    
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("your score is: ", score, "out of: ", len(questions))
    return  

run_test(questions)             