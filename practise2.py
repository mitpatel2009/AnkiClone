import tkinter as tk

root = tk.Tk()
root.title("Multi Screen Template")
root.geometry("400x300")

screens = {}

def show_screen (screen_name) :
    for screen in screens.values():
        screen.pack_forget()
    screens[screen_name].pack(fill=tk.BOTH,expand = True)

#Home Screen Frame
home_frame = tk.Frame(root)
label_home = tk.Label(home_frame,text="This is a home screen").pack()
button_home = tk.Button(home_frame,text="create",command=lambda:show_screen("create_screen")).pack()
button_home2 = tk.Button(home_frame,text="update",command=lambda:show_screen("update_screen")).pack()

create_frame = tk.Frame(root)
create_label = tk.Label(create_frame,text="This is a create screen").pack()
create_button= tk.Button(create_frame,text="screen1",command=lambda:show_screen("screen_1")).pack()
create_button2 = tk.Button(create_frame,text="screen2",command=lambda:show_screen("screen_2")).pack()

screen1_frame = tk.Frame(root)
screen1_label = tk.Label(screen1_frame,text="This is a screen1 screen").pack()
screen1_button= tk.Button(screen1_frame,text="home",command=lambda:show_screen("home")).pack()

screen2_frame = tk.Frame(root)
screen2_label = tk.Label(screen2_frame,text="This is a screen2 screen").pack()
screen2_button= tk.Button(screen2_frame,text="home",command=lambda:show_screen("home")).pack()

update_frame = tk.Frame(root)
update_label = tk.Label(update_frame,text="This is a update screen").pack()
update_button= tk.Button(update_frame,text="home",command=lambda:show_screen("home")).pack()



screens["home"] = home_frame
screens["create_screen"] = create_frame
screens["screen_1"] = screen1_frame
screens["screen_2"] = screen2_frame
screens["update_screen"] = update_frame


show_screen("home")

root.mainloop()