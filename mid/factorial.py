n = int(input("請輸入一正整數 : "))
ans = 0
while True :
    if n < 0 :
        n = int(input("請輸入大於等於0的數字 : "))
    else :
        break
for i in range(n+1) :
    ans +=i
print(ans)