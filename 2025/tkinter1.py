import tkinter as tk

def convert_fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result.config(text=f"{celsius:.2f} °C")

root = tk.Tk()
root.title("Temperature Converter")

label_fahrenheit = tk.Label(root, text="Fahrenheit:")
label_fahrenheit.pack()

entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.pack()

button_convert = tk.Button(root, text="Convert", command=convert_fahrenheit_to_celsius)
button_convert.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
