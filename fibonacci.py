num = int(input("Digite um número: "))

fibonacci_1 = 0
fibonacci_2 = 1

found = False
while not found:
    if fibonacci_1 == num:
        found = True
        print(f"O número {num} pertence à sequência de Fibonacci.")
    elif fibonacci_1 > num:
        found = True
        print(f"O número {num} não pertence à sequência de Fibonacci.")
    else:
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
