import numpy as np
from typing import List
import cv2 as cv
from time import time, asctime

filename = '1.png'
img = cv.imread(filename)


def scale_img(frame, scale_percent):  # функция, для изменения размера изображения.
    # Принимает два аргумента scale_img( изображение в виде numpy массива, процент уменшения изображения))
    width = int(frame.shape[1] * scale_percent / 100)  # записываем в перемнные уменьшенные ширину и высоту
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)  # записываем их в tuple
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)  # уменьшаем по заданным параметрам
    return frame  # возвращаем уменьшенное изображение


def inPolygon(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and
                (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
            c = 1 - c
    return c


def bs(seq: List[int], res: int) -> int:  # Реализация бинарного поиска
    # на вход принимает список прямоугольник, и центр элепса по X
    # Выводит номер элемента в спсике, к которому ближе всего заданная координата Х
    seq = list(map(lambda x: x[1][0], seq))
    l = 0
    r = len(seq) - 1
    while abs(l - r) > 1:
        mid = (l + r) // 2
        if seq[mid] > res:
            r = mid
        else:
            l = mid
    return (l + r) // 2


def volt(img, pos_circle):  # Функция принимает изображение  и координаты центра элепса
    # Возвращает значение в вольтах, к которому значение центра ближе всего
    # hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # edge = cv.Canny(img, 75, 200)
    f = open("settins.txt", "r")
    try:
        min_max = list(map(int, f.readlines()[0].split(" ")))
    except ValueError:
        print("Предыдущие этапы настройки завершены неправильно, переделайте их")
        return
    try:
        sr = list(list(f.readlines()[3].split("\n"))[0].split("QQQ"))
    except ValueError:
        print("Предыдущие этапы настройки завершены неправильно, переделайте их")
        return

    for i in range(len(sr)):
        sr[i] = list(sr[i].split(","))
        for j in range(len(sr[i])):
            sr[i][j] = list(sr[i][j].split(" "))

    mask1 = cv.inRange(img, (min_max[0], min_max[1], min_max[2]), (min_max[3], min_max[4], min_max[5]))

    y, x, _ = img.shape

    contours0, hierarchy = cv.findContours(mask1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    sp = []

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

    # pos_circle = [773, 94]

    sp = sorted(sp, key=lambda x: x[1][0])

    # for i in sp:
    #     print(i)
    #     print("              ")
    # cv.imshow("",img)

    cv.waitKey(0)
    res = bs(sp, pos_circle[0])

    if res == 0:
        for i in range(1, 100):
            res = bs(sp, pos_circle[0 + i])
            if res != 0:
                return res
    else:
        return res


def volt_(pos_circle, bg_v):
    sp = []  # надо придумать как записывать и считывать его
    res = bs(sp, pos_circle[0])

    if res == 0:
        for i in range(1, 100):
            res = bs(sp, pos_circle[0 + i])
            if res != 0:
                return res + bg_v
    else:
        return res + bg_v

def writer(a) -> str:
    f = open("res.csv", "a")
    f.write(asctime() + ", {v}\n".format(v=a))

# cam = cv.VideoCapture(1)
#
# while True:
#     _, frame = cam.read()
#
#     print(volt(frame, [250, 20]))
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
