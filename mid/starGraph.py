N = int(input("請輸入一個數字 : "))
for i in range(N) :  
    print('*'*(i+1))
for i in range(N) :  
    print(' '*i,end='')
    print('*'*(N-i))
'''
*
**
***
****
*****
*****
 ****
  ***
   **
    *
'''
for i in range(N) :  
    print(' '*(N-(i+1)),end='')
    print('*'*(i+1))
for i in range(N) :  
    print('*'*(N-i))
''' 
    *
   **
  ***
 ****
*****
*****
****
***
**
*
'''
# ------------------------------------ #
for i in range(N) :  
    print('*'*(i+1),end='')
    print(' '*((N-(i+1))*2),end='')
    print('*'*(i+1))
    '''
    = print('*'*(i+1),' '*((N-(i+1))*2),'*'*(i+1),sep='')
    '''

for i in range(N) :  
    print(' '*(i),end='')
    print('*'*((N-(i))*2),end='')
    print(' '*(i))
'''
*        *
**      **
***    ***
****  ****
**********
**********
 ********
  ******
   ****
    **
'''
# ------------------------------------ #
for i in range(N) :  
    print('*'*(i+1),end='')
    print(' '*((N-(i+1))*2),end='')
    print('*'*(i+1))

for i in range(N) :  
    print('*'*(N-(i)),end='')
    print(' '*(i*2),end='')
    print('*'*(N-(i)))
'''
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''
for i in range(N) :  
    print('*'*(i+1),end='')
    print(' '*((N-(i+1))*2),end='')
    print('*'*(i+1))

for i in range(N) :  
    print('*'*(N-(i+1)),end='')
    print(' '*((i+1)*2),end='')
    print('*'*(N-(i+1)))
'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''