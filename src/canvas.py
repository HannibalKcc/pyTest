from tkinter import *


class PaintApp:

    def __init__(self, master):
        self.master = master
        self.color = "black"
        self.brush_size = 5
        self.erase_mode = False
        self.drawWidgets()
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        if self.erase_mode:
            x1, y1 = (event.x - int(self.brush_size)), (event.y - int(self.brush_size))
            x2, y2 = (event.x + int(self.brush_size)), (event.y + int(self.brush_size))
            self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
        else:
            x1, y1 = (event.x - int(self.brush_size)), (event.y - int(self.brush_size))
            x2, y2 = (event.x + int(self.brush_size)), (event.y + int(self.brush_size))
            self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def change_brush_size(self, new_size):
        self.brush_size = new_size

    def change_color(self, new_color):
        self.color = new_color

    def toggle_erase_mode(self):
        self.erase_mode = not self.erase_mode

    def drawWidgets(self):
        self.controls = Frame(self.master, pady=10)
        self.controls.pack(side=TOP)
        self.brush_label = Label(self.controls, text="Brush size: ")
        self.brush_label.pack(side=LEFT)
        self.brush_slider = Scale(self.controls, from_=1, to=10, orient=HORIZONTAL, command=self.change_brush_size)
        self.brush_slider.set(self.brush_size)
        self.brush_slider.pack(side=LEFT)
        self.color_label = Label(self.controls, text="Color: ")
        self.color_label.pack(side=LEFT)
        self.color_menu = OptionMenu(self.controls, StringVar(), "black", "red", "green", "blue",
                                     command=self.change_color)
        self.color_menu.pack(side=LEFT)
        self.erase_button = Button(self.controls, text="Eraser", command=self.toggle_erase_mode)
        self.erase_button.pack(side=LEFT)
        self.canvas = Canvas(self.master, width=500, height=500)
        self.canvas.pack()


root = Tk()
root.title("Paint App")
paint_app = PaintApp(root)
root.mainloop()
