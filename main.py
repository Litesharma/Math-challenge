import random
SIGNS=['-','*','+']
MIN_NUM = 2
MAX_NUM = 12
TOTAL_PROBLEMS=10
def generate_problem(MIN_NUM,MAX_NUM):
    left=random.randint(MIN_NUM,MAX_NUM)
    right=random.randint(MIN_NUM,MAX_NUM)
    operator=random.choice(SIGNS)
    exp=f'{left} {operator} {right}'
    ans=eval(exp)
    return exp,ans


print("Game start :)")
for i in range(TOTAL_PROBLEMS):
    problem,answer=generate_problem(MIN_NUM,MAX_NUM)
    while True:
        user_answer=int(input(f'\nproblem #{i+1}\n{problem} = '))
        if user_answer==answer:
            break

        
        


    
