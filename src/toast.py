import tkinter as tk
import time

def show_toast(message, duration=2):
    toast = tk.Toplevel()
    toast.overrideredirect(1)  # 隐藏窗口边框
    toast.geometry("+%d+%d" % (toast.winfo_screenwidth() // 2, toast.winfo_screenheight() // 2))
    toast.configure(bg="lightgray")

    label = tk.Label(toast, text=message, bg="lightgray", fg="black", font=("Helvetica", 12))
    label.pack(padx=20, pady=10)

    toast.after(int(duration * 1000), toast.destroy)  # 设置持续时间，然后销毁窗口
    toast.mainloop()

if __name__ == "__main__":
    show_toast("Hello, this is a toast message!", duration=2)