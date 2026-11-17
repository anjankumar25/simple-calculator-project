import tkinter as tk

def calculate():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        c = operator.get()

        if c == "+":
            result = a + b

        elif c == "-":
            result = a - b

        elif c == "*":
            result = a * b

        elif c == "/":
            if b == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = a / b

        elif c == "%":
            if b == 0:
                result_label.config(text="Cannot divide by zero")
                return
            result = (a / b) * 100

        elif c == "^":
            result = a ** 2

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers")


# Main window
root = tk.Tk()
root.title("My Calculator")
root.geometry("350x400")
root.configure(bg="#eaf2f8")

# Heading
heading = tk.Label(
    root,
    text="SIMPLE CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="#eaf2f8"
)
heading.pack(pady=20)

# First number
tk.Label(root, text="Enter First Number", bg="#eaf2f8").pack()
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=8)

# Second number
tk.Label(root, text="Enter Second Number", bg="#eaf2f8").pack()
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=8)

# Operator selection
tk.Label(root, text="Select Operator", bg="#eaf2f8").pack(pady=5)

operator = tk.StringVar()
operator.set("+")

menu = tk.OptionMenu(root, operator, "+", "-", "*", "/", "%", "^")
menu.config(font=("Arial", 12))
menu.pack(pady=5)

# Calculate button
button = tk.Button(
    root,
    text="CALCULATE",
    command=calculate,
    bg="#2874a6",
    fg="white",
    font=("Arial", 12, "bold")
)
button.pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 16, "bold"),
    bg="#eaf2f8"
)
result_label.pack(pady=10)

# Run application
root.mainloop()