A="sfvn"
B="jnvl"
C=[]
def fun(A,B,C):
    if(len(A)==0): 
        return C.append(B)
    if(len(B)==0):
        return C.append(A)
    if A[0] > B[-1]:
        
        C.append(A[0])
        fun(A[1:], B, C)
    else:
        C.append(B[-1])
        fun(A, B[:-1], C)
fun(A,B,C)
str= ""
for i in C:
    str+=i
print(str)
    