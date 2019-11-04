count = int(input("請輸入一正整數 : "))

def fib(count) :
    if count == 1 :
        return 1 
    elif count == 0 :
        return 0
    else :
        return fib(count-1) + fib(count - 2) 

ans = fib(count)
print(ans)