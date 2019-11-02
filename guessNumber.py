import random
ans = random.randint(1,100)
min = 1
max = 100
while True :
    userGuess = int(input(f"請輸入一個介於 {min} ~ {max} 的值 :"))
    if  max > userGuess > min : 
        if userGuess > ans :
            max = userGuess 
        if userGuess < ans :
            min = userGuess
        if userGuess == ans :
            break
    else :
        print(f"輸入數字範圍不在{min} ~ {max}")
print(f"恭喜猜中，答案為{ans}")