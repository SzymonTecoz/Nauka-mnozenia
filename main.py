import random
import tkinter as tk

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

def check_correctness():
    try:
        a = int(answer_entry.get())
        if correct_answer == a:
            result_label.config(text= "Poprawna odpowiedź!")
        else:
            result_label.config(text= "Niepoprawna odpowiedź.")
    except ValueError:
        result_label.config(text = "Proszę wprowadzić poprawną liczbę")

def new_question():
    global b, wynik, correct_answer
    b, wynik, correct_answer = generate_case()
    question_label.config(text = f"Jaka liczba pomnożona przez {b} da nam {wynik}?")
    answer_entry.delete(0, tk.END)
    result_label.config(text = "")


b, wynik, correct_answer =generate_case()

app = tk.Tk()
app.title("Nauka mnożenia")

question_label = tk.Label(app, text = f"Jaka liczba pomnożona przez {b} da nam {wynik}?", font=("Helvetica", 14))
question_label.pack(pady=20)

answer_entry = tk.Entry(app, font=("Helvetica", 14))
answer_entry.pack(pady=10)

check_button = tk.Button(app, text="Sprawdź!", command=check_correctness, font=("Helvetica", 14))
check_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 14))
result_label.pack(pady=20)

new_question_button = tk.Button(app, text="Nowe pytanie", command=new_question, font=("Helvetica", 14))
new_question_button.pack(pady=10)

app.mainloop()