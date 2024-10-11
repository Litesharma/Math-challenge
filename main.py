import random
signs=['-','x','+']
max_num = 12
min_num = 2
answer = 0
def generate_problem(min_num,max_num):
    global answer
    left=random.randint(min_num,max_num)
    right=random.randint(min_num,max_num)
    operator=random.choice(signs)
    if operator=='+':
        answer=left+right
    elif operator=='-':
        answer=left-right
    else:
        answer=left*right

    return f'{left} {operator} {right} = '


def check_answer(answer,user_answer):
    return answer==user_answer
print("Game start :)")
n=1
problem=generate_problem(min_num,max_num)
user_answer=int(input(f'{problem}'))
while n<5:
    result=check_answer(answer,user_answer)
    if not result:
        user_answer=int(input(f'{problem}'))
        
    else:
        problem=generate_problem(min_num,max_num)
        user_answer=int(input(f'{problem}'))
        n+=1
    
        
        


    
