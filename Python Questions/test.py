def answer(n):
    # make n+1 coefficients
    coefficients = [1]+[0]* n
    #go through all the combos
    for i in range(1, n+1):
        #start from the back and go down until you reach the middle
        for j in range(n, i-1, -1):
            
            coefficients[j] += coefficients[j-i]
            
    return coefficients[n] - 1

print(answer(10))