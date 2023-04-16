import tkinter as tk
from PIL import Image, ImageDraw
from tensorflow import keras
import os
import numpy as np

class DrawingBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.model = keras.models.load_model(os.path.join(os.path.dirname(__file__), 'mnist_cnn.h5'))
        self.title("28x28 Drawing Board")
        self.canvas = tk.Canvas(self, width=280, height=280, bg="white")
        self.canvas.pack()
        self.draw_grid()
        self.bind_events()

        self.clear_button = tk.Button(self, text="Clear", command=self.clear_board)
        self.clear_button.pack()

        self.save_button = tk.Button(self, text="Test Num", command=self.test_num)
        self.save_button.pack()

    def draw_grid(self):
        for i in range(0, 280, 10):
            for j in range(0, 280, 10):
                self.canvas.create_rectangle(i, j, i + 10, j + 10, outline="lightgray", width=1)

    def bind_events(self):
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<Button-1>", self.draw)

    def draw(self, event):
        x1, y1 = (event.x // 10) * 10, (event.y // 10) * 10
        x2, y2 = x1 + 10, y1 + 10
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", width=0, tags="content")

    def clear_board(self):
        self.canvas.delete("content")

    def test_num(self):
        img = Image.new("L", (28, 28), color=0)
        draw = ImageDraw.Draw(img)

        for content in self.canvas.find_withtag("content"):
            coords = self.canvas.coords(content)
            x1, y1, x2, y2 = [coord // 10 for coord in coords]
            draw.rectangle([x1, y1, x2, y2], fill=255)

        image_data = np.array(img)
        image_data = image_data.astype('float32')
        image_data /= 255  # 归一化像素值到 [0, 1] 范围
        image_data = np.expand_dims(image_data, axis=0)  # 扩展维度以匹配模型输入要求
        image_data = np.expand_dims(image_data, axis=-1)  # 为灰度图像添加通道维度
        # 使用模型进行预测
        prediction = self.model.predict(image_data)
        predicted_class = np.argmax(prediction, axis=-1)
        print("Predicted class:", predicted_class[0])


if __name__ == "__main__":
    __file__
    app = DrawingBoard()
    app.mainloop()