import tkinter as tk
import os
import sys

def button_yes_action():
    sad_window = tk.Toplevel(window)
    sad_window.geometry("300x150")
    sad_window.title("Очень жаль")

    label = tk.Label(sad_window, text="Очень жаль, папка system32 будет удалена с Вашего компьютера...", font=("Arial", 14), wraplength=280)
    label.pack(pady=30)

    countdown_label = tk.Label(sad_window, text="Осталось: 5 секунд", font=("Arial", 12))
    countdown_label.pack(pady=10)

    def update_countdown(seconds):
        countdown_label.config(text=f"Осталось: {seconds} секунд")
        if seconds > 0:
            sad_window.after(1000, update_countdown, seconds - 1)
        else:
            if sys.platform == "darwin":
                # Для macOS команда выключения
                os.system("sudo shutdown -h now")
            else:
                # Для Windows
                os.system("shutdown /s /t 1")

    update_countdown(5)

    button = tk.Button(sad_window, text="Да", command=lambda: os.system("shutdown /s /t 1") if sys.platform != "darwin" else os.system("sudo shutdown -h now"), font=("Arial", 12), bg="red", fg="white")
    button.pack(pady=10)

def button_no_action():
    new_window = tk.Toplevel(window)
    new_window.geometry("300x150")
    new_window.title("Отлично!")

    label = tk.Label(new_window, text="Ура, жду с нетерпением!", font=("Arial", 14), wraplength=280)
    label.pack(pady=30)

    def close_app():
        window.quit()
        new_window.quit()

    button = tk.Button(new_window, text="И я!", command=close_app, font=("Arial", 12), bg="blue", fg="white")
    button.pack()

def button_no_in_first_window():
    confirm_window = tk.Toplevel(window)
    confirm_window.geometry("300x150")
    confirm_window.title("Ты уверена?")

    label = tk.Label(confirm_window, text="Ты уверена?", font=("Arial", 14))
    label.pack(pady=30)

    button_yes = tk.Button(confirm_window, text="Да", command=button_yes_action, font=("Arial", 12), bg="green", fg="white")
    button_yes.pack(side=tk.LEFT, padx=20)

    button_no = tk.Button(confirm_window, text="Нет", command=button_no_action, font=("Arial", 12), bg="red", fg="white")
    button_no.pack(side=tk.RIGHT, padx=20)

def button_yes_action_in_first_window():
    new_window = tk.Toplevel(window)
    new_window.geometry("300x150")
    new_window.title("Отлично!")

    label = tk.Label(new_window, text="Ура, жду с нетерпением нашей встречи!", font=("Arial", 14), wraplength=280)
    label.pack(pady=30)

    def close_app():
        window.quit()
        new_window.quit()

    button = tk.Button(new_window, text="И я!", command=close_app, font=("Arial", 12), bg="blue", fg="white")
    button.pack()

window = tk.Tk()
window.overrideredirect(True)
window.geometry("400x300")

label = tk.Label(window, text="Мы идем на свидание?", font=("Arial", 14))
label.pack(pady=50)

button_yes = tk.Button(window, text="Да", command=button_yes_action_in_first_window, font=("Arial", 16), width=10, height=3, bg="green", fg="white")
button_yes.pack(side=tk.LEFT, padx=20)

button_no = tk.Button(window, text="Нет", command=button_no_in_first_window, font=("Arial", 16), width=10, height=3, bg="red", fg="white")
button_no.pack(side=tk.RIGHT, padx=20)

window.mainloop()

# push to creating .app file