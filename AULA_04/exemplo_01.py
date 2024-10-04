# Try e excep para criar uma proteção para o site caso o usuário insira algum valor não requisitado e de erro, ou que o usuário divida por zero

try:

    n1 = int(input("Insira o primeiro número inteiro"))
    n2 = int(input("Insira o segundo número inteiro"))
except ValueError:
    print("Verifique a entrada de dados")

else:

    try:
        result = n1 / n2
    
    except ZeroDivisionError:

        print("Não é possível dividir por zero!")
    else:    
        print(f"O Resultado da sua divisão é: {result:.2f}")



