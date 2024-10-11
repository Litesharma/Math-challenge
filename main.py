import random
import time
SIGNS=['-','*','+']
MIN_NUM = 2
MAX_NUM = 12
TOTAL_PROBLEMS=10
def generate_problem(MIN_NUM,MAX_NUM):
    left=random.randint(MIN_NUM,MAX_NUM)
    right=random.randint(MIN_NUM,MAX_NUM)
    operator=random.choice(SIGNS)
    exp=f'{left}{operator}{right}'
    ans=eval(exp)
    return exp,ans


print("Press enter to start : ")
print('-'*24)
start_time=time.time()
for i in range(TOTAL_PROBLEMS):
    problem,answer=generate_problem(MIN_NUM,MAX_NUM)
    while True:
        user_answer=int(input(f'problem #{i+1} {problem} = '))
        if user_answer==answer:
            break
end_time=time.time()
total_time=end_time-start_time
print(f'Well done! you take {round(total_time)} seconds')

        
        


    
