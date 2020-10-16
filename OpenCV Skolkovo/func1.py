import cv2 as cv
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


class rz(tk.Tk):
    rect_cords = []
    rectangls = []

    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        cam = cv.VideoCapture(0)
        _, img = cam.read()

        # img = Image.open("a.jpg")

        try:
            a, b, _ = scale_img(cutting_img(img), 200).shape
        except cv.error:
            print("Пожалуйста, перезапустите приложение и начните настройку заново, произошла ошибка")
            return

        self.canvas = tk.Canvas(self, width=b, height=a, cursor="cross")
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
        cam = cv.VideoCapture(0)
        _, img = cam.read()
        try:
            img = scale_img(cutting_img(img), 200)
        except cv.error:
            print("Пожалуйста, перезапустите приложение и начните настройку заново, произошла ошибка")
            return
        cv.imwrite("a.jpg", img)
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
        self.rect_cords.append([[str(self.start_x), str(event.x), str(event.x), str(self.start_x)],
                                [str(self.start_y), str(self.start_y), str(event.y), str(event.y)]])

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


def recognition_zone():
    app = rz()
    app.mainloop()
    f = open('settins.txt', 'a')
    l = []
    for i in app.rect_cords:
        i[0] = " ".join(i[0])
        i[1] = " ".join(i[1])

    for i in app.rect_cords:
        i = ",".join(i)
        l.append(i)
    l = "QQQ".join(l)
    f.write(l + "\n")


def nothing(x): pass


def cutting_img(frame):
    # Функция выделения части изображения, принимает на вход изображение с двумя зелеными квадратами
    # и возвращает обрезанное по ним
    f = open("settins.txt", "r")
    try:
        min_max = list(map(int, f.readlines()[0].split(" ")))
    except ValueError:
        print("Предыдущие этапы настройки завершены неправильно, переделайте их")
        return
    clone = frame
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  # переводим изображение в цветовое пространство HSV
    # mask1 = cv.inRange(hsv, (56, 107, 116), (98, 176, 255))
    # print((min_max[0], min_max[1], min_max[2]), (min_max[3], min_max[4], min_max[5]))
    mask1 = cv.inRange(hsv, (min_max[0], min_max[1], min_max[2]), (min_max[3], min_max[4], min_max[5]))
    # Биноризуем по порогам (минимальный - 2 аргумент, максимальный - 3, HSV - соответственно)

    # mask1 = cv.erode(mask1, (10, 10), iterations=3)
    # mask1 = cv.erode(mask1, (50, 50), iterations=3)
    # mask1 = cv.dilate(mask1, (5,5), iterations=10)
    # mask1 = cv.erode(mask1, (50, 50), iterations=3)

    contours, _ = cv.findContours(mask1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # ищем конутры на бинорезованнном изображении
    contours = sorted(contours, key=cv.contourArea, reverse=True)  # сортируем их по площади
    w_c = [contours[0], contours[1]]  # Записываем два самых больших контура в список
    list_for_quad = []  # создаем список  для прмоугольников
    for cnt in w_c:  # Проходимся по  самым большим контурам
        rect = cv.minAreaRect(cnt)  # вписываем в них прямоугольник
        # box = cv.boxPoints(rect)
        # box = np.int0(box)
        # cv.drawContours(frame, [box], 0, (255, 0, 0), 2)
        list_for_quad.append(rect)  # записываем координаты вписанного прямоугольника в список
    # - int(list_for_quad[0][1][1]) // 2
    x1 = (int(list_for_quad[0][0][0]) + int(list_for_quad[0][1][0]) // 4,
          int(list_for_quad[0][0][1]))  # Записываем координаты левого верхнего угла

    x2 = (int(list_for_quad[1][0][0]) - int(list_for_quad[1][1][0]) // 2,  # тут было -85
          int(list_for_quad[1][0][1]) + int(
              list_for_quad[1][1][1]) // 2)  # Записываем координаты правого ниженего угла, тут было -10
    # col = (0, 255, 0)

    # cv.rectangle(frame,x1, x2,col, int(3))
    #  cl = clone[x1[1]:x2[1], x1[0]:x2[0]]  # обрезаем изображение по координатам углов
    cl = clone[x2[1]:x1[1], x2[0]:x1[0]]  # обрезаем изображение по координатам углов

    return cl  # возвращаем его


def inPolygon(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and
                (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
            c = 1 - c
    return c


def scale_img(frame, scale_percent):  # функция, для изменения размера изображения.
    # Принимает два аргумента scale_img( изображение в виде numpy массива, процент уменшения изображения))
    width = int(frame.shape[1] * scale_percent / 100)  # записываем в перемнные уменьшенные ширину и высоту
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)  # записываем их в tuple
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)  # уменьшаем по заданным параметрам
    return frame  # возвращаем уменьшенное изображение


def rectangle_img(img):
    f2 = open("res.csv", "w")
    f2.write("Время, Значение (Вольты)\n")
    f = open('settins.txt', 'w')
    f.close()
    y, x, _ = img.shape
    x1 = int(x * 40 / 1280)
    y1 = int(y * 259 / 720)
    x2 = int(x - x * 40 / 1280)
    y2 = int(y - y * 159 / 720)
    cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
    return img


def yellow_eleps():
    cam = cv.VideoCapture(0)

    cv.namedWindow('result')

    cv.createTrackbar('min_h', 'result', 0, 255, nothing)
    cv.createTrackbar('min_s', 'result', 0, 255, nothing)
    cv.createTrackbar('min_v', 'result', 0, 255, nothing)

    cv.createTrackbar('max_h', 'result', 0, 255, nothing)
    cv.createTrackbar('max_s', 'result', 0, 255, nothing)
    cv.createTrackbar('max_v', 'result', 0, 255, nothing)
    while 1:
        _, img = cam.read()
        img = scale_img(img, 200)
        img = cutting_img(img)
        try:
            hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        except cv.error:
            print("Пожалуйста, перезапустите приложение и начните настройку заново, произошла ошибка")
            return
        min_h = cv.getTrackbarPos('min_h', 'result')
        min_s = cv.getTrackbarPos('min_s', 'result')
        min_v = cv.getTrackbarPos('min_v', 'result')

        max_h = cv.getTrackbarPos('max_h', 'result')
        max_s = cv.getTrackbarPos('max_s', 'result')
        max_v = cv.getTrackbarPos('max_v', 'result')

        # Normal masking algorithm
        lower_blue = np.array([min_h, min_s, min_v])
        upper_blue = np.array([max_h, max_s, max_v])

        mask = cv.inRange(hsv, lower_blue, upper_blue)
        cv.imshow("mask", mask)
        if cv.waitKey(1) & 0xFF == ord('q'):
            f = open('settins.txt', 'a')

            stroka = str(min_h) + " " + str(min_s) + " " + str(min_v) + " " + str(max_h) + " " + str(max_s) + " " + str(
                max_v)

            f.write(stroka + "\n")
            break

    cam.release()
    cv.destroyAllWindows()


def greenQuads():
    cam = cv.VideoCapture(0)

    cv.namedWindow('result')

    cv.createTrackbar('min_h', 'result', 0, 255, nothing)
    cv.createTrackbar('min_s', 'result', 0, 255, nothing)
    cv.createTrackbar('min_v', 'result', 0, 255, nothing)

    cv.createTrackbar('max_h', 'result', 0, 255, nothing)
    cv.createTrackbar('max_s', 'result', 0, 255, nothing)
    cv.createTrackbar('max_v', 'result', 0, 255, nothing)
    while 1:
        _, img = cam.read()
        img = scale_img(img, 200)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        min_h = cv.getTrackbarPos('min_h', 'result')
        min_s = cv.getTrackbarPos('min_s', 'result')
        min_v = cv.getTrackbarPos('min_v', 'result')

        max_h = cv.getTrackbarPos('max_h', 'result')
        max_s = cv.getTrackbarPos('max_s', 'result')
        max_v = cv.getTrackbarPos('max_v', 'result')

        # Normal masking algorithm
        lower_blue = np.array([min_h, min_s, min_v])
        upper_blue = np.array([max_h, max_s, max_v])

        mask = cv.inRange(hsv, lower_blue, upper_blue)
        cv.imshow("mask", mask)
        if cv.waitKey(1) & 0xFF == ord('q'):
            f = open('settins.txt', 'a')

            stroka = str(min_h) + " " + str(min_s) + " " + str(min_v) + " " + str(max_h) + " " + str(max_s) + " " + str(
                max_v)
            f.write(stroka + "\n")
            break

    cam.release()
    cv.destroyAllWindows()


def chert():
    sp = []
    f = open("settins.txt", "r")

    cam = cv.VideoCapture(0)

    cv.namedWindow('result')

    cv.createTrackbar('min_b', 'result', 0, 255, nothing)
    cv.createTrackbar('min_g', 'result', 0, 255, nothing)
    cv.createTrackbar('min_r', 'result', 0, 255, nothing)

    cv.createTrackbar('max_b', 'result', 0, 255, nothing)
    cv.createTrackbar('max_g', 'result', 0, 255, nothing)
    cv.createTrackbar('max_r', 'result', 0, 255, nothing)
    try:
        sr = list(list(f.readlines()[3].split("\n"))[0].split("QQQ"))
    except IndexError:
        print("Предыдущие этапы настройки завершены неправильно, переделайте их")
        return
    for i in range(len(sr)):
        sr[i] = list(sr[i].split(","))
        for j in range(len(sr[i])):
            try:
                sr[i][j] = list(map(int, sr[i][j].split(" ")))
            except ValueError:
                print("Предыдущие этапы настройки завершены неправильно, переделайте их")
                return

    while 1:
        sp.clear()
        score = 0
        _, img = cam.read()
        img = scale_img(img, 200)
        img = cutting_img(img)

        min_h = cv.getTrackbarPos('min_b', 'result')
        min_s = cv.getTrackbarPos('min_g', 'result')
        min_v = cv.getTrackbarPos('min_r', 'result')

        max_h = cv.getTrackbarPos('max_b', 'result')
        max_s = cv.getTrackbarPos('max_g', 'result')
        max_v = cv.getTrackbarPos('max_r', 'result')

        lower_blue = np.array([min_h, min_s, min_v])
        upper_blue = np.array([max_h, max_s, max_v])
        try:
            mask = cv.inRange(img, lower_blue, upper_blue)
        except cv.error:
            print("Пожалуйста, перезапустите приложение и начните настройку заново, произошла ошибка")
            return

        y, x, _ = img.shape
        contours0, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for cnt in contours0:
            rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
            box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
            box = np.int0(box)  # округление координат
            y1 = box[2][1]
            x1 = box[2][0]

            area = int(rect[1][0] * rect[1][1])  # вычисление площади
            if area < 5: continue
            c = 0
            for i in sr:
                if inPolygon(x1, y1, i[0], i[1]) == 1:
                    break
                else:
                    c += 1
            if c == len(sr): continue

            cv.drawContours(img, [box], 0, (0, 255, 0), 1)
            sp.append(box)
            score += 1
        cv.putText(img, str(score), (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        cv.imshow("mask", mask)
        cv.imshow("img", img)

        if cv.waitKey(1) & 0xFF == ord('q'):
            f = open('settins.txt', 'a')
            sp = sorted(sp, key=lambda x: x[1][0])
            print(sp)

            stroka = str(min_h) + " " + str(min_s) + " " + str(min_v) + " " + str(max_h) + " " + str(max_s) + " " + str(
                max_v)

            f.write(stroka + "\n")
            break

    cam.release()
    cv.destroyAllWindows()


# cam = cv.VideoCapture(0)
#
# while True:
#     _, frame = cam.read()
#     frame = scale_img(frame, 200)
#     frame = rectangle_img(frame)
#     cv.imshow('Video', frame)
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cam.release()
# cv.destroyAllWindows()

greenQuads()

# yellow_eleps()

# chert()

# recognition_zone()
