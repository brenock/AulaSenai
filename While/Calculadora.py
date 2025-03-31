import time
print("Seja bem vindo a cauculadora do breno!")

while True:
    time.sleep(0.5)
    print("Digite 1 para adição")
    print("Digite 2 para subtração")
    print("Digite 3 para multiplicação")
    print("Digite 4 para divisão")
    print("digite 6 para sair")

    desisao = int(input('O que você quer fazer: '))
    if desisao == 1:
     print("Você esta na cauculadora de adição!")
     nmra =int(input("Digite o primeiro numero: "))
     nmrb = int(input('Digite o segundo numero: '))
     soma = nmra + nmrb
     print(f"A soma dos numeros {nmra} + {nmrb} = {soma}")

     continue

    elif desisao == 2:
     print("Você esta na calculadora de subtração")
     nmrc = int(input("Digite o primeiro numero: "))
     nmrd = int(input("Digite o segundo numero: "))
     sbtr = nmrc - nmrd
     print(f"A subtração dos numeros {nmrc} - {nmrd} = {sbtr}")git 