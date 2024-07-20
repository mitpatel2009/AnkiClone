#Importing Additional Extensions
import tkinter as tk
import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk

#Creating empty list
screens = {}

def on_button_click():
    show_screen("home")

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)

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

button3 = tk.Button(button_frame, text="Add Card", font=("Helvetica", 27), bg="#DC6B19", width=10, height=1, command=lambda: show_add_card_screen())
button3.pack(pady=20, padx=window_width // 4, ipadx=30, ipady=15)

screens["home"] = root_frame

# Screen 2
deck_frame = tk.Frame(root)
deck_frame.pack()
deck_frame.configure(bg="#6C0345")

# Load and resize the image
image_path1 = "C:\\Users\\MIT\\Downloads\\house.png.png"
resized_image1 = resize_image(image_path1, 150, 160)  # Adjust width and height as needed

# Create a button with the resized image
button1 = tk.Button(deck_frame, image=resized_image1, command=on_button_click)
button1.place(x=10, y=10)

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

def search():
    search_term = search_entry.get(1.0, END).strip()
    cursor.execute("SELECT front, back FROM card WHERE front LIKE %s OR back LIKE %s", (f"%{search_term}%", f"%{search_term}%"))
    results = cursor.fetchall()
    for item in tree.get_children():
        tree.delete(item)
    for row in results:
        tree.insert("", "end", values=row)

add_question_frame = tk.Frame(root)
add_question_frame.configure(bg="#6C0345")

# Load and resize the image
image_path2 = "C:\\Users\\MIT\\Downloads\\house.png.png"
resized_image2 = resize_image(image_path2, 150, 160)  # Adjust width and height as needed

# Create a button with the resized image
button2 = tk.Button(add_question_frame, image=resized_image2, command=on_button_click)
button2.place(x=10, y=10)

heading_label = tk.Label(add_question_frame, text="Search", font=("Helvetica", 36), bg="#6C0345", fg="black")
heading_label.pack(pady=10)

search_label = tk.Label(add_question_frame, text="Search:", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
search_label.pack()

search_entry = tk.Text(add_question_frame, height="3", width="40")
search_entry.pack()

search_button = tk.Button(add_question_frame, text="Search", bg="#6C0345", fg="#DC6B19", height="2", width="25", font=("Helvetica, 20"), command=search)
search_button.pack(pady=10)

# screen 3

def populate_treeview():
    cursor.execute("SELECT deck,front, back FROM card")  
    for row in cursor.fetchall():
     tree.insert("", "end", values=row)

tree_frame = tk.Frame(add_question_frame)
tree_frame.pack(pady=10)

tree = ttk.Treeview(tree_frame, columns=("Deck","Front", "Back"), show="headings", selectmode="browse")

tree.heading("Deck", text= "Deck")

tree.heading("Front", text="Front")
tree.heading("Back", text="Back")

vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)


tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)


tree.grid(row=0, column=0, sticky="nsew")
vsb.grid(row=0, column=1, sticky="ns")
hsb.grid(row=1, column=0, sticky="ew")


tree_frame.grid_rowconfigure(0, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)
populate_treeview()
screens["add_question"] = add_question_frame

# Screen 4
add_card_frame = tk.Frame(root)
add_card_frame.configure(bg="#6C0345")

def update_deck_dropdown():
    cursor.execute("SELECT deck_id, deck_name FROM deck")
    decks = cursor.fetchall()
    deck_names = [deck[1] for deck in decks]
    deck_combobox['values'] = deck_names

def add_question():
    selected_deck = deck_combobox.get()
    cursor.execute("SELECT deck_id FROM deck WHERE deck_name = %s", (selected_deck,))
    deck_id = cursor.fetchone()[0]
    front_text = front_entry.get()
    back_text = back_entry.get()
    cursor.execute("INSERT INTO card (deck_id,deck,front, back) VALUES (%s, %s, %s,%s)", (deck_id, front_text, back_text,selected_deck))
    db.commit()

# Load and resize the image
image_path3 = "C:\\Users\\MIT\\Downloads\\house.png.png"
resized_image3 = resize_image(image_path3, 150, 160)  # Adjust width and height as needed

# Create a button with the resized image
button3 = tk.Button(add_card_frame, image=resized_image3, command=on_button_click)
button3.place(x=10, y=10)

deck_label = tk.Label(add_card_frame, text="Deck:", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
deck_label.pack()
deck_combobox = ttk.Combobox(add_card_frame, font=("Helvetica", 20))
deck_combobox.pack()

# Add labels and text boxes
front_label = tk.Label(add_card_frame, text="Front:", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
front_label.pack()
front_entry = tk.Entry(add_card_frame, font=("Helvetica", 20))
front_entry.pack()

back_label = tk.Label(add_card_frame, text="Back:", font=("Helvetica", 25), bg="#6C0345", fg="#DC6B19")
back_label.pack()
back_entry = tk.Entry(add_card_frame, font=("Helvetica", 20))
back_entry.pack()

# Add button
add_button = tk.Button(add_card_frame, text="Add Question", bg="#6C0345", fg="#DC6B19", font=("Helvetica", 20), command=add_question)
add_button.pack(pady=10)
screens["add_card"] = add_card_frame

def show_add_card_screen():
    update_deck_dropdown()
    show_screen("add_card")

show_screen("home")

root.geometry(f"{window_width}x{window_height}")
root.mainloop