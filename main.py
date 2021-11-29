from tkinter import *
from PIL import ImageTk, Image
import time

# ---------------------------- CONSTANTS ------------------------------- #

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"
WORK_MIN=0.1
SHORT_BR_MIN=0.1
LONG_BR_MIN=0.5
reps=0

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
   pass
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
   global reps
   reps+=1
   work_sec=WORK_MIN*60
   short_break_sec=SHORT_BR_MIN*60
   long_break_sec=LONG_BR_MIN*60
   if reps%8==0:
      count_down(long_break_sec)
      timer.config(fg=RED, text="BREAK")
   elif  reps%2==0:
      count_down(short_break_sec)
      timer.config(fg=PINK,text="BREAK")
   else:
      if reps<8:
         count_down(work_sec)
         timer.config(fg=GREEN, text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
   mins_upd, secs_upd = (time // 60, time% 60)
   if secs_upd<10:
      secs_upd=f"0{secs_upd}"
   if mins_upd<10:
      mins_upd=f"0{mins_upd}"
   canv.itemconfig(timer_text,text=f"{mins_upd}:{secs_upd}")
   if time>0:
      window.after(1000, count_down, time - 1)
   else:
      start()
# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer=Label(text="Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start_btn=Button(text="Start", font=(FONT_NAME, 20), command = start)
start_btn.grid(column=0, row=2)
reset_btn=Button(text="Reset", font=(FONT_NAME, 20), command=reset)
reset_btn.grid(column=2, row=2)

img = ImageTk.PhotoImage(Image.open("tomato.png")) # PIL
canv.create_image(100, 112, image = img)
timer_text=canv.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canv.grid(column=1, row=1)

check_mark=Label(text="✔", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()