import random

def generate_case():
    b = random.randint(1,50)
    wynik = random.randint (10, 100)
    while wynik % b != 0:
        b = random.randint(1,50)
        wynik = random.randint(10,100)
    print(f"b = {b}")
    print(f"wynik = {wynik}")
    correct_answer = wynik/b
    return b, wynik, correct_answer

def check_correctness(b, wynik, correct_answer):
    a = int(input("Jaka liczba pomnożona przez b daje nam wynik?\n"))
    if correct_answer == a:
        print("Poprawna odpowiedź")
    else:
        print("Błąd")

b, wynik, correct_answer =generate_case()
check_correctness(b, wynik, correct_answer)