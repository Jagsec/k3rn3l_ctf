from pwn import *
from sympy import *
context.log_level = 'debug' #will print all input and output for debugging purposes
conn = remote("ctf.k3rn3l4rmy.com", 2236) #enter the address and the port here as strings. For example nc 0.0.0.0 5000 turns into remote('0.0.0.0', 5000)
def get_input(): #function to get one line from the netcat
    input = conn.recvline().strip().decode()
    return input
def parse(polynomial):
    '''
    TODO: Parse polynomial
    For example, parse("x^3 + 2x^2 - x + 1") should return [1,2,-1,1]
    '''
    polynomes = polynomial.split()
    new_polynomes = []
    for polynome in polynomes:
        if not polynome.startswith('x'):
            new_polynomes.append(polynome.replace('x', '*x'))
        else:
            new_polynomes.append(polynome)
    new_polynomial = ''.join(new_polynomes)
    new_polynomial = new_polynomial.replace('^','**')
    x = Symbol('x')
    poly = polys.polytools.poly_from_expr(new_polynomial)[0]
    return poly.coeffs(), poly.monoms()
for _ in range(4): get_input() #ignore challenge flavortext
for i in range(100):
    type = get_input()
    coeffs, monoms = parse(get_input())
    exponent = monoms[0][0]
    if exponent%2 == 0:
        multiplier = 1
    else:
        multiplier = -1
    print(coeffs)
    ans = -1
    if 'sum of the roots' in type:
        root_sum = -coeffs[1]/coeffs[0]
        ans = root_sum
    #TODO: Find answer
    elif 'sum of the reciprocals of the roots' in type:
        roots_product = (coeffs[-1]/coeffs[0])*multiplier
        roots_product_sum = (-coeffs[-2]/coeffs[0])*multiplier
        reciprocal_sum = roots_product_sum/roots_product
        ans = reciprocal_sum
    #TODO: Find answer
    elif 'sum of the squares of the roots' in type:
        squared_roots_sum = (coeffs[1]/coeffs[0])**2 - 2*(coeffs[2]/coeffs[0])
        ans = (squared_roots_sum)
    #TODO: Find answer
    print(ans)
    conn.sendline(str(ans)) #send answer to server
    get_input()
conn.interactive() #should print flag if you got everything right
