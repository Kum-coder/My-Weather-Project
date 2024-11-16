from tkinter import *
from tkinter import ttk
import requests

def data_get():
    try:
        city = city_name.get()
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5448d933be14281d81b3b87978ae751"
        ).json()

        if data.get("cod") != 200:
            w_label1.config(text="Error")
            wd_label1.config(text="Invalid city")
            temp_label1.config(text="")
            pressure_label1.config(text="")
            return

        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(int(data['main']['temp'] - 273.15)))
        pressure_label1.config(text=data['main']['pressure'])
    except Exception as e:
        w_label1.config(text="Error")
        wd_label1.config(text="Check connection")
        temp_label1.config(text="")
        pressure_label1.config(text="")

win = Tk()
win.title("My Weather App")
win.config(bg="blue")
win.geometry("500x570")

# Title Label
new_label = Label(
    win, text="Kumar's Weather Update", font=("Time New Roman", 20, "bold")
)
new_label.place(x=25, y=50, height=50, width=450)

# Combobox for city selection
city_name = StringVar()
list_name = ["Patna", "Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore", "Hyderabad","China","Masbate-City"]
com = ttk.Combobox(
    win,
    values=list_name,
    font=("Time New Roman", 20, "bold"),
    textvariable=city_name,
    state="readonly",
)
com.place(x=25, y=120, height=50, width=450)

# Weather Information Labels
w_label = Label(win, text="Weather Update", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)
w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wd_label = Label(win, text="Weather Description", font=("Time New Roman", 17))
wd_label.place(x=25, y=330, height=50, width=210)
wd_label1 = Label(win, text="", font=("Time New Roman", 17))
wd_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)
temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

pressure_label = Label(win, text="Pressure", font=("Time New Roman", 20))
pressure_label.place(x=25, y=470, height=50, width=210)
pressure_label1 = Label(win, text="", font=("Time New Roman", 20))
pressure_label1.place(x=250, y=470, height=50, width=210)

# Button to fetch data
done_button = Button(
    win, text="Done", font=("Time New Roman", 20, "bold"), command=data_get
)
done_button.place(x=200, y=190, height=50, width=100)

win.mainloop()
