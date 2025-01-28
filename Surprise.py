import tkinter as tk
from tkinter import messagebox
import random

# Define some surprises
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The purpose of our lives is to be happy. - Dalai Lama",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Get busy living or get busy dying. - Stephen King",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
]

math_facts = [
    "The Fibonacci sequence is encoded in the number 1/89.",
    "A circle has infinite lines of symmetry.",
    "Zero is the only real number that is neither positive nor negative.",
    "The square root of 2 is irrational.",
    "A googol (10^100) is larger than the number of atoms in the observable universe.",
]

physics_facts = [
    "Light from the Sun takes about 8 minutes to reach Earth.",
    "Nothing can travel faster than the speed of light (299,792,458 m/s).",
    "Energy and mass are interchangeable, as per E=mc^2.",
    "Black holes can slow down time due to their immense gravity.",
    "The universe is expanding at an accelerating rate.",
]

fun_facts = [
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries arenβ€™t.",
    "Honey never spoils. Archaeologists have found 3000-year-old honey in tombs.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
    "Wombat poop is cube-shaped.",
]

# Combine all surprises
all_surprises = quotes + math_facts + physics_facts + fun_facts

# Function to display a random surprise
def surprise_me():
    surprise = random.choice(all_surprises)
    messagebox.showinfo("Surprise!", surprise)

# Create the main application window
root = tk.Tk()
root.title("Surprise Me!")
root.geometry("400x400")
root.configure(bg="#2c3e50")

# Add a label
label = tk.Label(root, text="Click the button for a surprise!", 
                 font=("Helvetica", 16, "bold"), 
                 bg="#2c3e50", fg="white")
label.pack(pady=50)

# Add a beautiful button
surprise_button = tk.Button(root, 
                             text="Surprise Me!", 
                             font=("Helvetica", 14, "bold"), 
                             bg="#1abc9c", 
                             fg="white", 
                             activebackground="#16a085", 
                             activeforeground="white", 
                             relief="raised", 
                             bd=10,
                             command=surprise_me)
surprise_button.pack(pady=20)

# Run the application
root.mainloop()
