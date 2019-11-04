n = int(input("請輸入一正整數 : "))
while True:
    if n >= 2 :
        break
    else :
        n = int(input("請輸入大於等於2的數 : "))
if n%2 == 0 :
    print(f'{n}是偶數')
else :
    print(f'{n}是奇數')