import random

def generate_case():
    b = random.randint(1,50)
    wynik = random.randint (10, 100)
    while wynik % b != 0:
        b = random.randint(1,10)
        wynik = random.randint(10,100)
    print(b)
    print(wynik)
    correct_answer = wynik/b

generate_case()