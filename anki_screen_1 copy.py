import tkinter as tk
import mysql.connector
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

screens = {}

def show_screen(screen_name):
    for screen in screens.values():
        screen.pack_forget()
    screens[screen_name].pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Anki")
window_width = 1200
window_height = 900

# Screen 1
root_frame = tk.Frame(root)
root_frame.pack()
root_frame.configure(bg="#6C0345")
root.configure(bg="#6C0345")

heading_label = tk.Label(root_frame, text="Anki", font=("Helvetica", 36), bg="#6C0345", fg="black")
heading_label.pack(pady=window_height // 10)
heading_label.configure(bg="#6C0345")

button_frame = tk.Frame(root_frame)
button_frame.pack()
button_frame.configure(bg="#6C0345")

button1 = tk.Button(button_frame, text="Deck", font=("Helvetica", 27), bg="#DC6B19", width=10, height=1, command=lambda: show_screen("deck"))
button1.pack(pady=20, padx=window_width // 4, ipadx=30, ipady=15)

button2 = tk.Button(button_frame, text="Search", font=("Helvetica", 27), bg="#DC6B19", width=10, height=1, command=lambda: show_screen("add_question"))
button2.pack(pady=20, padx=window_width // 4, ipadx=30, ipady=15)

button3 = tk.Button(button_frame, text="Add Card", font=("Helvetica", 27), bg="#DC6B19", width=10, height=1,command=lambda:show_screen("add_card"))
button3.pack(pady=20, padx=window_width // 4, ipadx=30, ipady=15)

screens["home"] = root_frame

# Screen 2
deck_frame = tk.Frame(root)
deck_frame.pack()
deck_frame.configure(bg="#6C0345")

heading_label = tk.Label(deck_frame, text="Deck", font=("Helvetica", 36), bg="#6C0345", fg="black")
heading_label.pack(pady=10)

listbox = tk.Listbox(deck_frame, width=30, height=10, font=("Helvetica", 12))
listbox.pack(pady=17)

create_deck_lbl = tk.Label(deck_frame, text="Enter Deck Name Here: ", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
create_deck_lbl.pack(pady=10)

# Establish connection to MySQL database
db = mysql.connector.connect(user='root', password='iamcool1@3',
                             host='127.0.0.1',
                             database='anki_clone')

cursor = db.cursor()

def insert_deck():
    deck_name = deck_txtbox1.get(1.0, END).strip()
    cursor.execute("INSERT INTO deck (deck_name) VALUES (%s)", (deck_name,))
    db.commit()
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT deck_name FROM deck")
    decks = cursor.fetchall()
    for deck in decks:
        listbox.insert(tk.END, deck[0])
    deck_txtbox1.delete("1.0", END)

deck_txtbox1 = tk.Text(deck_frame, height="2.5", width="40")
update_listbox()
deck_txtbox1.pack()

deck_btn = tk.Button(deck_frame, text="Create Deck", bg="#6C0345", fg="#DC6B19", height="2", width="25", font=("Helvetica, 20"), command=insert_deck)
deck_btn.pack(side="bottom")
screens["deck"] = deck_frame


def on_button_click():
    label.config(text="Button clicked! Navigating to home page...")
    show_screen("home")

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)



# Load and resize the image
image_path = "C:\\Users\\MIT\\Downloads\\house.png.png"
resized_image = resize_image(image_path, 150, 160)  # Adjust width and height as needed

# Create a button with the resized image
button = tk.Button(root, image=resized_image, command=on_button_click)
button.place(x=10,y=10)

# Create a label to display the button click message
label = tk.Label(root, text="Click this button to go home page")
label.pack(pady=10,padx=1)





# Screen 3
def search():
    search_term = search_entry.get(1.0, END).strip()
    # Implement search functionality here

add_question_frame = tk.Frame(root)
add_question_frame.configure(bg="#6C0345")

heading_label = tk.Label(add_question_frame, text="Search", font=("Helvetica", 36), bg="#6C0345", fg="black")
heading_label.pack(pady=10)

search_label = tk.Label(add_question_frame, text="Search:", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
search_label.pack()

search_entry = tk.Text(add_question_frame, height="3", width="40")
search_entry.pack()

search_button = tk.Button(add_question_frame, text="Search", bg="#6C0345", fg="#DC6B19", height="2", width="25", font=("Helvetica, 20"), command=search)
search_button.pack(pady=10)
screens["add_question"] = add_question_frame


#screen4
add_card_frame = tk.Frame(root)
add_card_frame.configure(bg="#6C0345")
# Add heading
heading_label = tk.Label(add_card_frame, text="Add Question", font=("Arial", 18))
heading_label.pack(pady=10)

# Add labels and text boxes
deck_label = tk.Label(add_card_frame, text="Deck:")
deck_label.pack()
deck_entry = tk.Entry(add_card_frame)
deck_entry.pack()

front_label = tk.Label(add_card_frame, text="Front:")
front_label.pack()
front_entry = tk.Entry(add_card_frame)
front_entry.pack()

back_label = tk.Label(add_card_frame, text="Back:")
back_label.pack()
back_entry = tk.Entry(add_card_frame)
back_entry.pack()

# Add button
add_button = tk.Button(add_card_frame, text="Add Question", )
add_button.pack(pady=10)
screens["add_card"] = add_card_frame

show_screen("home")
root.geometry(f"{window_width}x{window_height}")
root.mainloop()
