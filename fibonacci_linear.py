import sys


                        #means int will be return (expect int return from this)
def fibonacci(n: int) -> int:
    if n ==0:
        return 0
    if n==1:
        return 1
    
    last,next = 0,1
    for _ in range(n):
        temp = next
        next = last+next
        last = temp
        
        #above same with
        #next, last = last +next,next

    return last

print("what Python?",sys.version)

print(fibonacci(4))
print(fibonacci(8))