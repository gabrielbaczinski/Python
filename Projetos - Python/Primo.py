def primos(n):
    return n**2 - n + 41
    
def ehPrimo(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def par(n):
    return 2*n + 6

#n = 41
#print(f'{primos(n)} - {ehPrimo(n)}')
#print(par())
