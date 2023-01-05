import random

def sortear():
    numero = random.randint(0, 60)
    return numero
def perguntar():
    a = input("Deseja jogar novamente [S/N]? ").upper()
    return a
def repetidos():
    print("Números repetidos!", num1, num2, num3, num4, num5, num6)


while True:
    num1 = str(sortear())
    num2 = str(sortear())
    num3 = str(sortear())
    num4 = str(sortear())
    num5 = str(sortear())
    num6 = str(sortear())

    if num1 == num2 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num6:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    elif num2 == num1 or num2 == num3 or num2 == num4 or num2 == num5 or num2 == num6:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    elif num3 == num1 or num1 == num2 or num1 == num4 or num1 == num5 or num1 == num6:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    elif num4 == num1 or num1 == num3 or num1 == num2 or num1 == num5 or num1 == num6:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    elif num5 == num1 or num1 == num3 or num1 == num4 or num1 == num2 or num1 == num6:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    elif num6 == num1 or num1 == num3 or num1 == num4 or num1 == num5 or num1 == num2:
        repetidos()
        if perguntar() == 'S':
            continue
        else:
            break
    else:
        print("Os números sorteados para você testar a sorte na Mega da Virada foram:\n", num1, num2, num3, num4, num5, num6)
        with open("NúmerosSorteados.txt", 'a') as arquivo:
            arquivo.write("\nOs números sorteados anteriores foram:\n")
            arquivo.write(num1)
            arquivo.write('-')
            arquivo.write(num2)
            arquivo.write('-')
            arquivo.write(num3)
            arquivo.write('-')
            arquivo.write(num4)
            arquivo.write('-')
            arquivo.write(num5)
            arquivo.write('-')
            arquivo.write(num6)
        break