from tkinter import *
import pandas as pd
import random

import pandas.errors

BACKGROUND_COLOR = "#B1DDC6"
try:
    WORD_LIST = pd.read_csv("data/words_to_learn.csv")
except pandas.errors.EmptyDataError:
    WORD_LIST = pd.read_csv("data/french_words.csv")
WORDS = WORD_LIST.to_dict(orient="records")
word_index = ""


def select_wrong():
    next_word()


def select_right():
    WORDS.remove(WORDS[word_index])
    list_to_learn = pd.DataFrame.from_dict(WORDS)
    list_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


def flip_card():
    canvas.itemconfig(canvas_image, image=CARD_BACK_IMAGE)
    english_word = WORDS[word_index]['English']
    top_label.config(text="English", bg=BACKGROUND_COLOR, highlightthickness=0)
    bottom_label.config(text=english_word, bg=BACKGROUND_COLOR, highlightthickness=0)


window = Tk()
window.title("Flashy")
window.config(height=1000, width=900, padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
canvas.grid(row=0, column=0, columnspan=2)

top_label = Label(text="French", font=("Arial", 40, "italic"), bg="white")
top_label.place(x=325, y=150)
bottom_label = Label(text="French Text Here", font=("Arial", 60, "bold"), bg="white")
bottom_label.place(x=400, y=300, anchor="center")

WRONG_IMAGE = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=WRONG_IMAGE, command=select_wrong, highlightthickness=0)
wrong_button.grid(row=1, column=0)
RIGHT_IMAGE = PhotoImage(file="images/right.png")
right_button = Button(image=RIGHT_IMAGE, command=select_right, highlightthickness=0)
right_button.grid(row=1, column=1)


def next_word():
    global word_index, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=CARD_FRONT_IMAGE)
    word_index = random.randint(0, len(WORDS) - 1)
    french_word = WORDS[word_index]['French']
    top_label.config(text="French", bg="white")
    bottom_label.config(text=french_word, bg="white")
    flip_timer = window.after(3000, func=flip_card)


next_word()

window.mainloop()
