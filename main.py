import tkinter as tk
import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

arts = [Rock, Paper, Scissors]

player_score = 0
computer_score = 0

def play(player_choice):
    global player_score, computer_score

    computer_choice = random.randint(0, 2)

    result = f"You chose:\n{arts[player_choice]}\n"
    result += f"Computer chose:\n{arts[computer_choice]}\n"

    if player_choice == computer_choice:
        result += "\nDraw!"
    elif (
        (player_choice == 0 and computer_choice == 2) or
        (player_choice == 1 and computer_choice == 0) or
        (player_choice == 2 and computer_choice == 1)
    ):
        result += "\nYou Win! 🎉"
        player_score += 1
    else:
        result += "\nYou Lose! 😢"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")

root = tk.Tk()
root.title("ASCII Rock Paper Scissors")
root.geometry("800x700")

title = tk.Label(root, text="Choose Your Move", font=("Arial", 16))
title.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text=Rock, font=("Courier", 8),
                     command=lambda: play(0))
rock_btn.grid(row=0, column=0, padx=10)
rock_label= tk.Label(button_frame, text="Rock", font=("Arial", 10))
rock_label.grid(row=1, column=0)
paper_btn = tk.Button(button_frame, text=Paper, font=("Courier", 8),
                      command=lambda: play(1))
paper_btn.grid(row=0, column=1, padx=10)
paper_label = tk.Label(button_frame, text="Paper", font=("Arial", 10))

paper_label.grid(row=1, column=1)

scissors_btn = tk.Button(button_frame, text=Scissors, font=("Courier", 8),
                         command=lambda: play(2))
scissors_btn.grid(row=0, column=2, padx=10)
scissors_label = tk.Label(button_frame, text="Scissors", font=("Arial", 10))
scissors_label.grid(row=1, column=2)

result_label = tk.Label(root, text="Make your move!",
                        font=("Courier", 10), justify="left")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Player: 0 | Computer: 0",
                       font=("Arial", 14))
score_label.pack()

root.mainloop()
