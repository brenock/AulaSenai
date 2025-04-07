import time

carros = ["Fusca","Gol","Palio","Uno"]
print(f"Lista de carros:{carros}")
for carro, carros in enumerate(carros):
    time.sleep(0.5),print(carro,carros)
