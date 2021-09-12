import datetime as dt

time=dt.datetime.now()

hour= (time.hour)

if hour<12:
    greeting="Good Morning"

elif hour>=12 and hour<17:
    greeting="Good Afternoon"

elif hour>=17 and hour<=24
    greeting="Good Evening"

greet=Label(main_f, text=greeting, font=(Arial,20), bg="#565050", fg="#06EBB4")