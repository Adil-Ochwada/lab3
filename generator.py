import random
import time
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
import pygame

pygame.mixer.init()
pygame.mixer.music.load("gta.mp3")  
pygame.mixer.music.play(-1)

def generate_block():
    letters = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3)
    digits = random.choices("0123456789", k=2)
    block_elements = letters + digits
    random.shuffle(block_elements)
    return "".join(block_elements)

def generator():
    try:
        
        key = "-".join(generate_block() for _ in range(3))
        
        
        key_field.config(state="normal")
        key_field.delete(1.0, "end")
        key_field.insert("end", key)
        key_field.config(state="disabled")
        
        
        animate_key()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def animate_key():
    for _ in range(3):
        key_field.config(bg="yellow")
        window.update()
        time.sleep(0.1)
        key_field.config(bg="white")
        window.update()
        time.sleep(0.1)

window = tk.Tk()
window.title("Генератор ключей")
window.geometry("700x450")

bg_img = Image.open("dcs.jpg") 
bg_img = bg_img.resize((700, 450), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)

bg_lbl = tk.Label(window, image=bg_photo)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

lbl = tk.Label(window, text="Генератор ключей", font=("Arial", 24, "bold"), bg="#000000", fg="white")
lbl.pack(pady=10)

key_frame = tk.Frame(window, bg="black", padx=10, pady=10)
key_frame.pack(pady=20)
key_field = tk.Text(key_frame, font=("Courier", 18), width=20, height=1, state="disabled", bg="white", fg="black")
key_field.pack()

btn = tk.Button(window, text="Cгенерируйте ключ", font=("Arial", 16), command=generator, bg="#008CBA", fg="white")
btn.pack(pady=10)


window.mainloop()

pygame.mixer.music.stop()
