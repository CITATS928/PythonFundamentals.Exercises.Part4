def fibonnaci(num):
    if num ==0:
        return 0                    #base case
    elif num ==1 or num==2:
        return 1                    #base case
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)

print(fibonnaci(10))