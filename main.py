from tkinter import *
from PIL import ImageTk, Image
import time
import math

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
timer_stopped=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
   window.after_cancel(timer_stopped)
   timer_lb.config(text="Timer")
   check_marks.config(text="")
   canv.itemconfig(timer_text, text="00:00")
   global reps
   reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
   global reps
   reps+=1
   work_sec=WORK_MIN*60
   short_break_sec=SHORT_BR_MIN*60
   long_break_sec=LONG_BR_MIN*60
   if reps%8==0:
      count_down(long_break_sec)
      timer_lb.config(fg=RED, text="BREAK")
   elif  reps%2==0:
      count_down(short_break_sec)
      timer_lb.config(fg=PINK, text="BREAK")
   else:
      if reps<8:
         count_down(work_sec)
         timer_lb.config(fg=GREEN, text="WORK")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
   mins_upd, secs_upd = (time // 60, time% 60)
   if secs_upd<10:
      secs_upd=f"0{secs_upd}"
   if mins_upd<10:
      mins_upd=f"0{mins_upd}"
   canv.itemconfig(timer_text,text=f"{mins_upd}:{secs_upd}")
   if time>0:
      global timer_stopped
      timer_stopped=window.after(1000, count_down, time - 1)
   else:
      start_timer()
      marks=""
      work_sessions=math.floor(reps/2)
      for _ in range(work_sessions):
         marks+="✔"
      check_marks.config(text=marks)
# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer_lb=Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_lb.grid(column=1, row=0)

start_btn=Button(text="Start", font=(FONT_NAME, 20), command = start_timer)
start_btn.grid(column=0, row=2)
reset_btn=Button(text="Reset", font=(FONT_NAME, 20), command=reset)
reset_btn.grid(column=2, row=2)

img = ImageTk.PhotoImage(Image.open("tomato.png")) # PIL
canv.create_image(100, 112, image = img)
timer_text=canv.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canv.grid(column=1, row=1)

check_marks=Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

