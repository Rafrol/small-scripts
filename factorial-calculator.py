def factorial(n):
    result = 1
    for i in range(n+1):
        if i == 0:
            result = result
        else:
            result = result * i
    return result
