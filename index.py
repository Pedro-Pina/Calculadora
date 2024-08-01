def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


print("Seleciona uma operação")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True: 
    escolha = input("Selecione os números entre [1, 2, 3, 4]: ")

    if escolha in ('1', '2', '3', '4'):
        try:
         num1 = float(input("Escolha algum número: "))
         num2 = float(input("Escolha mais um número: "))
        except ValueError:
            print("INVALIDO! Escolha algum NÚMERO.")

    if escolha == '1':
        print(num1, "+", num2, "=", soma(num1, num2))
    elif escolha == '2':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif escolha == '3':
        print(num1, "*", num2, "=", mult(num1, num2))
    elif escolha == '4':
        print(num1, "/", num2, "=", div(num1, num2))

    outro_calculo = input("Gostaria de fazer mas algum calculo? (sim/não): ")
    if outro_calculo == "não":
     break

    else:
        print("Invalido")