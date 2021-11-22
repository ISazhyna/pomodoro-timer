from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"

# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer=Label(text="Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start=Button(text="Start", font=(FONT_NAME, 20))
start.grid(column=0, row=2)
start=Button(text="Reset", font=(FONT_NAME, 20))
start.grid(column=2, row=2)

img = ImageTk.PhotoImage(Image.open("tomato.png")) # PIL
canv.create_image(100, 112, image = img)
canv.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canv.grid(column=1, row=1)

window.mainloop()