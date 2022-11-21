from covid import Covid
import tkinter
import pydantic
import requests

covid = Covid(source = "worldometers")
countryname = "s. korea" #change this to a country (USA for an example)
window = tkinter.Tk()

status = covid.get_status_by_country_name(countryname)

status_list = (list(status.values()))

new_cases = status_list[3]
new_death = status_list[5]

total_cases = status_list[1]
total_death = status_list[4]

window.title(countryname + " Covid Status")
window.geometry("450x300")
window.resizable(False, False)

country = tkinter.Label(window, text = countryname)
country.config(font = ("Gmarket Sans TTF", 20))
country.pack()

today = tkinter.Label(window, text = "Today")
today.place(x = 100, y = 65, anchor = "center")
today.config(font = ("Gmarket Sans TTF", 20))

today_cases = tkinter.Label(window, text = "Cases: " + str(new_cases))
today_cases.place(x = 100, y = 123, anchor = "center")
today_cases.config(font = ("Gmarket Sans TTF", 15))

today_death = tkinter.Label(window, text = "Deaths: " + str(new_death))
today_death.place(x = 100, y = 176, anchor = "center")
today_death.config(font = ("Gmarket Sans TTF", 15))

total = tkinter.Label(window, text = "Total")
total.place(x = 340, y = 65, anchor = "center")
total.config(font = ("Gmarket Sans TTF", 20))

all_cases = tkinter.Label(window, text = "Cases: " + str(total_cases))
all_cases.place(x = 340, y = 123, anchor = "center")
all_cases.config(font = ("Gmarket Sans TTF", 15))

all_deaths = tkinter.Label(window, text = "Deaths: " + str(total_death))
all_deaths.place(x = 340, y = 176, anchor = "center")
all_deaths.config(font = ("Gmarket Sans TTF", 15))


window.mainloop()
