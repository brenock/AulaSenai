import time
print("Seja bem vindo a cauculadora do breno!")

while True:
    time.sleep(0.5)
    print("Digite 1 para adição")
    time.sleep(0.1)
    print("Digite 2 para subtração")
    time.sleep(0.1)
    print("Digite 3 para multiplicação")
    time.sleep(0.1)
    print("Digite 4 para divisão")
    time.sleep(0.1)
    print("digite 5 para sair")
    time.sleep(0.5)
    print('')
    desisao = int(input('O que você quer fazer: '))

    if desisao == 1:
     print('')
     time.sleep(0.5)
     print("Você esta na cauculadora de adição!")
     nmra =int(input("Digite o primeiro número: "))
     nmrb = int(input('Digite o segundo número: '))
     soma = nmra + nmrb
     print(f"A soma dos numeros {nmra} + {nmrb} = {soma}")

     continue

    elif desisao == 2:
     print('')
     time.sleep(0.5)
     print("Você esta na calculadora de subtração")
     nmrc = int(input("Digite o primeiro número: "))
     nmrd = int(input("Digite o segundo número: "))
     sbtr = nmrc - nmrd
     print(f"A subtração dos numeros {nmrc} - {nmrd} = {sbtr}")

     continue

    elif desisao == 3:
     print('')
     time.sleep(0.5)
     print("Você esta na calculadora de multiplicação")
     nmre = int(input("Digite o primeiro número: "))
     nmrf = int(input("Digite o segundo número: "))
     mltp = nmre * nmrf
     print(f"A multiplicação entre os numeros {nmre} X {nmrf} = {mltp}")

     continue

    elif desisao == 4:
     print('')
     time.sleep(0.5)
     print("Você esta na calculadora de divisão")
     nmrg = int(input("Digite o primeiro número: "))
     nmrh = int(input("Digite o segundo número: "))
     divi = nmrg / nmrh
     print(f"A divisão entre os números {nmrg} / {nmrh} = {divi}")
     continue

    elif desisao == 5:
     print('')
     time.sleep(0.5)
     print("Obrigado por usar a calculadora")
     break
    else:
        print('')
        time.sleep(0.5)
        print("Erro, esse comando não existe!")

#Fim da caulculadora.








