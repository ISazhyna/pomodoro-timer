from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

img = ImageTk.PhotoImage(Image.open("tomato.png")) # PIL
canv.create_image(100, 112, image = img)
canv.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canv.pack()

window.mainloop()