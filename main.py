from tkinter import *
from PIL import ImageTk, Image
import time

# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
FONT_NAME = "Courier"

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
   window.update()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
   mins=int(canv.itemcget(timer_text, 'text')[:2])
   secs=int(canv.itemcget(timer_text, 'text')[-2:])
   time=mins*60+secs
   count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
   mins_upd, secs_upd = (time // 60, time% 60)
   if time>0:
      window.after(1000, count_down, time - 1)
   if secs_upd<10:
      secs_upd=f"0{secs_upd}"
   if mins_upd<10:
      mins_upd=f"0{mins_upd}"
   canv.itemconfig(timer_text,text=f"{mins_upd}:{secs_upd}")
# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer=Label(text="Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start=Button(text="Start", font=(FONT_NAME, 20), command = start)
start.grid(column=0, row=2)
start=Button(text="Reset", font=(FONT_NAME, 20), command=reset)
start.grid(column=2, row=2)

img = ImageTk.PhotoImage(Image.open("tomato.png")) # PIL
canv.create_image(100, 112, image = img)
timer_text=canv.create_text(100,112,text="01:00",fill="white",font=(FONT_NAME,35,"bold"))
canv.grid(column=1, row=1)

check_mark=Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()