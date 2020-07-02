'''Find the greates common denominator of two integers
Ex: GCD of 20 and 8 is 4
because 8/4 is 2 and 20/4 is 5
1 for two integers a and b, where a > b, divide a by b
2 If remainder r is 0 then stop ; GCD is b
3 Otherwise set a to b, b to r and repeat at step 1 until r is 0
'''

def gcd(a,b):
    while b!=0:
        t = a
        a = b
        b = t % b
    
    return a

print(gcd(60,96))
print(gcd(20,8))