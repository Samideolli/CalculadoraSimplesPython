"""Calculadora com while"""
while True:
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    num_validos = None
    n1f = 0
    n2f = 0

    try:
        n1f = float(n1)
        n2f = float(n2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print("Um ou ambos os números digitados são inválidos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Digite um operador válido!!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue
    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == "+":
        print(f"{n1}+{n2}=", n1f+n2f)
    elif operador == "-":
        print(f"{n1}-{n2}=",n1f-n2f)
    elif operador == "*":
        print(f"{n1}*{n2}=",n1f*n2f)  
    elif operador == "/":
        print(f"{n1}/{n2}=",n1f/n2f)  
    else:
        print("nunca deveria chegar aqui!")

    sair = input("Deseja sair? [s]im: ").lower().startswith('s')

    if sair:
        break