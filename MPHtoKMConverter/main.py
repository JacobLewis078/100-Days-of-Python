from tkinter import *

window = Tk()
window.minsize(width=200, height=100)
window.title("MPH to Kilometer")
window.config(padx=20, pady=20)


def mph_to_km():
    kmh.config(text=f"{user_input.get() * 1.60934} km per hour")


# Entry
user_input = IntVar()
mph = Entry(width=10, textvariable=user_input)
mph.grid(column=2, row=0)

# Labels
miles = Label(text="Miles", font=("Arial", 14, "normal"))
miles.grid(column=3, row=0)

is_equal_label = Label(text="is equal to ", font=("Arial", 14, "normal"))
is_equal_label.grid(column=1, row=1)

kmh = Label(text="", font=("Arial", 14, "normal"))
kmh.grid(column=2, row=1)


# button
calculate = Button(text="Calculate", command=mph_to_km)
calculate.grid(column=2, row=2)

window.mainloop()
