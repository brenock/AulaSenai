def apresentar(nome,idade,hobbie,voz):
    if voz == False:
        print("Precisa-se de um interprete.")
    else:
        print(f"Olá me chamo {nome}, tenho {idade} anos, e meu hobbie é {hobbie}")

(apresentar("Breno",16,"Jogar bola", True))
def soma(numero1,numero2):
    return numero1 + numero2
print(soma(10,10))
