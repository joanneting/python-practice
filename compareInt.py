print("請輸入三個整數")
F= int(input("請輸入第一個整數 : "))
S= int(input("請輸入第二個整數 : "))
T= int(input("請輸入第三個整數 : "))

if F > S :
    F, S = S, F
if F > T :
    F, T = T, F
if S > T :
    S, T = T, S

print(f'{F}<{S}<{T}')