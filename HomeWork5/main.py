import tkinter as tk
from os.path import isfile

timer = 100
score = 0
is_started = False
record_user = 0

if not isfile("record.txt"):
    with open("record.txt", "w") as file_record:
        file_record.write("0")
else:
    with open("record.txt", "r") as file_record:
        record_user = file_record.read()


# Обновление рекорда игры
def update_record():
    if score > int(record_user):
        with open("record.txt", "w") as file:
            file.write(str(score))
            show_record.config(text=f"Ваш текущий рекорд: {score}")


def click():
    global score
    global is_started
    if is_started and is_alive():
        score += 1


# Restart игры
def restart_game():
    global score
    global timer
    timer = 100
    score = 0


def start_game(event):
    global is_started
    if is_started is False:
        is_started = True
        hello_text.config(text="")
        update_display()
        update_time()


def update_display():
    global timer
    global score
    global is_started

    if timer > 80:
        bomb_image.config(image=img_1)
    elif timer > 40:
        bomb_image.config(image=img_2)
    elif timer > 0:
        bomb_image.config(image=img_3)
    else:
        bomb_image.config(image=img_4)
        update_record()

    score_text.config(text=f"Score: {score}")
    timer_text.config(text=f"Time: {timer}")

    root.after(100, update_display)


def update_time():
    global is_started
    global timer
    if is_started and is_alive():
        timer -= 1

    root.after(300, update_time)


def is_alive():
    global timer
    if timer < 1:
        timer = 0
        return False
    return True


root = tk.Tk()
root.title("first window")
root.config(bg="black")
root.geometry("800x800+600+0")
root.maxsize(1000, 1000)
root.minsize(1000, 1000)
root.resizable(False, False)

hello_text = tk.Label(
    master=root,
    text="Hello! Push the ENTER to start the game!",
    fg="aqua",
    bg="black",
    font=("Arial", 30, "bold")
)
hello_text.pack()

show_record = tk.Label(
    master=root,
    text=f"Ваш текущий рекорд: {record_user}",
    fg="red",
    bg="black",
    font=("Arial", 15, "bold")
)
show_record.pack()

timer_text = tk.Label(
    master=root,
    text=f"Time: {timer}",
    fg="aqua",
    bg="black",
    font=("Arial", 20, "bold")
)
timer_text.pack()

score_text = tk.Label(
    master=root,
    text=f"Score: {score}",
    fg="aqua",
    bg="black",
    font=("Arial", 20, "bold")
)
score_text.pack()

button_restart = tk.Button(
    text="RESTART GAME",
    bg="black",
    fg="aqua",
    font=("Arial", 20, "bold"),
    command=restart_game
)
button_restart.pack()

img_1 = tk.PhotoImage(file="images/1.png").subsample(2, 2)
img_2 = tk.PhotoImage(file="images/2.png").subsample(2, 2)
img_3 = tk.PhotoImage(file="images/3.png").subsample(2, 2)
img_4 = tk.PhotoImage(file="images/4.png").subsample(2, 2)

bomb_image = tk.Label(
    image=img_1
)
bomb_image.pack()

button_click = tk.Button(
    text="CLICK ME!!!!",
    bg="black",
    fg="aqua",
    font=("Arial", 20, "bold"),
    command=click
)
button_click.pack()

root.bind("<Return>", start_game)

root.mainloop()
