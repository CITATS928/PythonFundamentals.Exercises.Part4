def fac(num):
    if num ==0 or num ==1:
        return 1
    return num*fac(num-1)

print(fac(10))      #3_628_800
print(fac(5))       #120