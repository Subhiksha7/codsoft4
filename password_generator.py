import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0")

        # Define the character sets to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the generated password
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))

# Set up the main window
root = tk.Tk()
root.title("Password Generator")

# Set up the length label and entry
label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Set up the button to generate the password
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)

# Set up the entry to display the generated password
label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=50)
entry_password.pack(pady=5)

# Run the application
root.mainloop()
