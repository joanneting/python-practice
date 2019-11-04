def compareTotal(*addNumber,compare=0) :
    total = 0
    for n in addNumber:
        total += n
    if total > compare :
        print(f'總和 : {total}比{compare}大')
    elif total < compare :
        print(f'總和 : {total}比{compare}小')
    else :
        print(f'總和 : {total} 兩個相等')
compareTotal(1,2,3)
compareTotal(1,2,3,compare=3)
compareTotal(1,2,3,compare=6)
compareTotal(1,2,3,compare=9)
compareTotal(1,2,3,6,4,3,2,compare=14)

