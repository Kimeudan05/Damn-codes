import random
import tkinter as tk

def generate_quote():
    quotes = [
        {"quote": "The only way to do great work is to love what you do.", "author": "Masila Kimeu"},
        {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
        {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
        {"quote": "In the middle of every difficulty lies opportunity.", "author": "Kinyua James"},
        {"quote": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
        {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Ruth Mutiso"}
    ]
    quote_data = random.choice(quotes)
    quote = quote_data["quote"]
    author = quote_data["author"]
    return quote, author

def update_quote():
    quote, author = generate_quote()
    quote_label.config(text=quote)
    author_label.config(text=f"~ {author.upper()}", fg="red")

root = tk.Tk()
root.title("Quotes Generator")
root.geometry("720x250")

frame = tk.Frame(root)
frame.pack(padx=30, pady=40)

quote_label = tk.Label(frame, text="", font=("Helvetica", 35), wraplength=650)
quote_label.pack()

author_label = tk.Label(frame, text="", font=("Helvetica", 12))
author_label.pack(pady=10)

generate_button = tk.Button(frame, text="Generate Quote", command=update_quote)
generate_button.configure(
    font=("Helvetica", 12),
    bg="blue",
    fg="white",
    activebackground="darkblue",
    activeforeground="white",
    relief=tk.RAISED,
    padx=10,
    pady=10
)
generate_button.pack(pady=20)

root.mainloop()
