import sys

def findFactorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return str(fac)

def primeNumbers(n):
    l = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            l.append(str(i))
    return l

def fibonacci(n):
    l = [0, 1]
    a0, a1 = 0, 1
    for i in range(n - 2):
        temp = a1
        a1 = a1 + a0
        a0 = temp
        l.append(str(a1))
    return l

def main(method, value):
    if method == 'factorial':
        return findFactorial(value)
    elif method == 'primeNumbers':
        return primeNumbers(value)
    elif method == 'fibonacci':
        return fibonacci(value)
    else:
        return "invalid method"

if __name__ == '__main__':
    method = sys.argv[1]
    value = int(sys.argv[2])
    result = main(method, value)
    print(result)
