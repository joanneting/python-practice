import random

# method 1
array = [0,1,2,3,4,5,6,7,8,9]
i=0
while i < 10 :
    random.shuffle(array)
    numberArray = array[1:7]
    value = float(0)
    for j in numberArray :
        value += j
 #   average=round(value/6,2)
    average=value/6
    print(numberArray,f'average={average:.2f}')
    i+=1

print('----------------------------------------------')
# method 2
i=0
while i < 10 :
    i+=1
    #numberArray = [random.randint(0,9) for _ in range(6)]
    numberArray = random.sample(range(0,9),6)
    
    value = float(0)
    for j in numberArray :
        value += j
 #   average=round(value/6,2)
    average=value/6
    print(f'{i} : ',numberArray,f'average={average:.2f}')
     