import tkinter as tk
from PIL import Image, ImageTk


class ExampleApp(tk.Tk):
    rect_cords = []
    rectangls = []

    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        img = Image.open("a.jpg")
        a, b = img.size
        self.canvas = tk.Canvas(self, width=a, height=b, cursor="cross")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas.bind("<Button-3>", self.undof)
        self.rect = None

        self.start_x = None
        self.start_y = None

        self._draw_image()

    def _draw_image(self):
        self.im = Image.open('a.jpg')
        self.tk_im = ImageTk.PhotoImage(self.im)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_im)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        # #one rectangle
        # if not self.rect:
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1)
        self.rectangls.append(self.rect)

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY, )

    def on_button_release(self, event):
        self.rect_cords.append([[str(self.start_x), str(event.x),  str(event.x), str(self.start_x)], [str(self.start_y), str(self.start_y), str(event.y), str(event.y)]])

    def undof(self, event):
        try:
            self.canvas.delete(self.rectangls[-1])
            self.rectangls.pop()
            self.rect_cords.pop()
            self.printf()
        except:
            pass

    def printf(self):
        print(self.rect_cords)


if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()
    f = open('settins.txt', 'a')
    l  = []
    for i in app.rect_cords:
        i[0] = " ".join(i[0])
        i[1] = " ".join(i[1])

    for i in app.rect_cords:
        i = ",".join(i)
        l.append(i)
    l = "QQQ".join(l)
    f.write(l + "\n")




