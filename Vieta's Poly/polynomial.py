polynomial = 'x^13 + 76x^12 + 77x^11 - 95x^10 + 68x^9 - 31x^8 + 63x^7 + 67x^6 + 35x^5 - 9x^4 - 50x^3 + 43x^2 + 24x^1'
polynomes = polynomial.split()
print(polynomes)
new_polynomes = []
for polynome in polynomes:
    if not polynome.startswith('x'):
       new_polynomes.append(polynome.replace('x', '*x'))
    else:
        new_polynomes.append(polynome)
print(new_polynomes)
new_polynomial = ''.join(new_polynomes)
new_polynomial = new_polynomial.replace('^','**')
print(new_polynomial)