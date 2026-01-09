import requests
import random
import html

EDUCATION_CATEGORY_ID=9 #GK category

API_URL=f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_education_questions():
    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
        return None
    
def run_quiz():
    questions=get_education_questions()
    if not questions:
        print("Failed to fetch educational quetions")
        return
    score=0
    print("Welcome to the educational quiz!")

    for i,q in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrect=[html.unescape(a) for a in q['incorrect_answers']]

        options=incorrect+[correct]
        random.shuffle(options)

        print(f"question {i}:{question}")
        for idx, option in enumerate(options,1):
            print(f"{idx}.{option}")

        while True:
            try:
                choice=int(input(" your answer\n"))
                if i<=choice<=4:
                    break
            except ValueError:
                pass
        if options[choice-1]==correct:
            print("correct\n")
            score+=1
        else:
            print(f"X wrong! correct answer:{correct}\n")

    print(f"final score:{score}/{len(questions)}")
    print(f"percentage:{score}/{len(questions)*100:.1f}%")

if __name__=="__main__":
    run_quiz()