import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# Carregar perguntas
df = pd.read_excel('questions.xlsx')
questions = df.sample(n=10).values.tolist()

# Variáveis globais
score = 0
current_question = 0

# Função para verificar resposta
def check_answer(answer):
    global score, current_question

    if answer == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_results()

# Função para exibir próxima pergunta
def display_question():
    question, option1, option2, option3, option4, answer = questions[current_question]
    question_label.config(text=question)
    configure_buttons(option1, option2, option3, option4, answer)

# Função para configurar os botões
def configure_buttons(option1, option2, option3, option4, answer):
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))
    correct_answer.set(answer)

# Função para mostrar resultado final
def show_results():
    messagebox.showinfo("Quiz finalizado", f"Parabéns! Quiz finalizado.\n\nPontuação final: {score}/{len(questions)}")
    disable_buttons()
    play_again_btn.pack()

# Função para desabilitar os botões
def disable_buttons():
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)

# Função para jogar novamente
def play_again():
    global score, current_question, questions
    score = 0
    current_question = 0
    questions = df.sample(n=10).values.tolist()
    display_question()
    play_again_btn.pack_forget()

# Configuração da janela principal
janela = tk.Tk()
janela.title('Quiz')
janela.geometry("500x550")

background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"

janela.configure(bg=background_color)
janela.option_add('*Font', 'Arial')

# Ícone na tela
app_icon = PhotoImage(file="icon.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# Interface
question_label = tk.Label(janela, text="", wraplength=380, bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

# Botões de opções
option1_btn = tk.Button(janela, text=" ", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

option2_btn = tk.Button(janela, text=" ", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

option3_btn = tk.Button(janela, text=" ", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

option4_btn = tk.Button(janela, text=" ", width=30, bg=button_color, fg=button_text_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

# Botão de jogar novamente
play_again_btn = tk.Button(janela, command=play_again, text="Jogar Novamente", width=30, bg=button_color, fg=button_text_color, font=("Arial", 10, "bold"))

# Iniciar o quiz
display_question()
janela.mainloop()
