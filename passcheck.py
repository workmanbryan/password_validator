from tkinter import *
from PIL import Image, ImageTk


root = Tk(className="password validator")

capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_characters = ["!", '"', "#", "$", "%", "&", "'", "(", ")", "-", "=", "^", "~", "¥", "|", "@", "`", "[", "{", ";", "+", ":", "*", "]", "}", ",", "<", ".", ">", "/", "?", "_"]
length = []
caps = []
lowers = []
nums = []
chars = []

#requirements for password
def requirements():

    if 8 <= len(user_password.get()) <= 16:
        print("password is correct length")
        length.append(1)
        if 1 in length:
            length_label=Label(frame, text="Needs between 8 - 16 characters", font=(user_font), bg=bg_color, fg="#22dd66")
            length_label.grid(row=0, column=0, pady=3)
        else:
            pass
    else:
        length_label=Label(frame, text="Needs between 8 - 16 characters", font=(user_font), bg=bg_color, fg="#aa3333")
        length_label.grid(row=0, column=0, pady=3)

    for letter in user_password.get():
        if letter in capital_letters:
            print("Capital letter detected")
            caps.append(1)
            print(caps)
            if 1 in caps:
                capital_label=Label(frame, text="Needs at least 1 capital letter", font=(user_font), bg=bg_color, fg="#22dd66")
                capital_label.grid(row=1, column=0, pady=3)
            else:
                capital_label=Label(frame, text="Needs at least 1 capital letter", font=(user_font), bg=bg_color, fg="#aa3333")
                capital_label.grid(row=1, column=0, pady=3)   

    for letter in user_password.get():
        if letter in lower_letters:
            print("lowercase letter detected")
            lowers.append(1)
            if 1 in lowers:
                lowercase_label=Label(frame, text="Needs at least 1 lowercase letter", font=(user_font), bg=bg_color, fg="#22dd66")
                lowercase_label.grid(row=2, column=0, pady=3)
            else:
                lowercase_label=Label(frame, text="Needs at least 1 lowercase letter", font=(user_font), bg=bg_color, fg="#aa3333")
                lowercase_label.grid(row=2, column=0, pady=3) 
        
    for number in user_password.get():
        if number in numbers:
            print("number detected")
            nums.append(1)
            if 1 in nums:
                number_label=Label(frame, text="Needs at least 1 number", font=(user_font), bg=bg_color, fg="#22dd66")
                number_label.grid(row=3, column=0, pady=3)
            else:
                number_label=Label(frame, text="Needs at least 1 number", font=(user_font), bg=bg_color, fg="#aa3333")
                number_label.grid(row=3, column=0, pady=3)

    for char in user_password.get():
        if char in special_characters:
            print("special character detected")
            chars.append(1)
            if 1 in chars:
                special_label=Label(frame, text="Needs at least 1 special character", font=(user_font), bg=bg_color, fg="#22dd66")
                special_label.grid(row=4, column=0, pady=3)
            else:
                special_label=Label(frame, text="Needs at least 1 special character", font=(user_font), bg=bg_color, fg="#aa3333")
                special_label.grid(row=4, column=0, pady=3)


root.geometry("600x600")
bg_color = "#333333"
user_font = "Helvetica", 24
text_color = "#ffffff"
root.configure(bg=bg_color)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
frame = Frame(root)
frame1 = Frame(root)

frame.configure(bg=bg_color)
frame1.configure(bg=bg_color)

frame.grid(row=0, column=0)
frame1.grid(row=1, column=0)

#labels
length_label=Label(frame, text="Needs between 8 - 16 characters", font=(user_font), bg=bg_color, fg=text_color)
capital_label=Label(frame, text="Needs at least 1 capital letter", font=(user_font), bg=bg_color, fg=text_color)
lowercase_label=Label(frame, text="Needs at least 1 lowercase letter", font=(user_font), bg=bg_color, fg=text_color)
number_label=Label(frame, text="Needs at least 1 number", font=(user_font), bg=bg_color, fg=text_color)
special_label=Label(frame, text="Needs at least 1 special character", font=(user_font), bg=bg_color, fg=text_color)

#label formatting
length_label.grid(row=0, column=0, pady=3)
capital_label.grid(row=1, column=0, pady=3)
lowercase_label.grid(row=2, column=0, pady=3)
number_label.grid(row=3, column=0, pady=3)
special_label.grid(row=4, column=0, pady=3)

#User password input
user_password = StringVar()
password_entry = Entry(frame1, textvariable=user_password)
password_entry.grid(row=1, column=1)

password_entry_text=Label(frame1, text="Enter your password: ", font=(user_font), bg=bg_color, fg=text_color)
password_entry_text.grid(row=1, column=0)


#Button
submit_btn = Button(root, command=requirements, text="Check Password", font=("Baskerville",24), fg="#337755", height = 2, width = 16)
submit_btn.grid(row=2, column=0)

root.mainloop()
