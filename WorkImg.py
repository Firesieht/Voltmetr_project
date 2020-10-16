import cv2 as cv
import numpy as np
from typing import List
from time import time, asctime, sleep


# from .Hough import volt

# import imutils


def writer(a):
    f = open("OpenCV Skolkovo/res.csv", "a")
    f.write(asctime() + ", {v}\n".format(v=a))
    sleep(1)


def Application(rec_time, bg_v):
    n_time = time()
    cam = cv.VideoCapture(0)
    cord_circle = [100, 10]
    while True:
        _, frame = cam.read()
        c = scale_img(frame, 200)
        c = cutting_img(c)

        if cv.waitKey(1) & 0xFF == ord('t'):
            cord_circle[0] = int(input())

        d = volt_(cord_circle, bg_v)
        zp = open("zp.txt", "w")
        zp.write(str(d))

        cv.putText(c, str(d), (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

        cv.imshow(" ", c)
        if int(n_time - time()) % rec_time == 0:
            writer(d)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break


def scale_img(frame, scale_percent):  # функция, для изменения размера изображения.
    # Принимает два аргумента scale_img( изображение в виде numpy массива, процент уменшения изображения))
    width = int(frame.shape[1] * scale_percent / 100)  # записываем в перемнные уменьшенные ширину и высоту
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)  # записываем их в tuple
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)  # уменьшаем по заданным параметрам
    return frame  # возвращаем уменьшенное изображение


def cutting_img(frame):
    # Функция выделения части изображения, принимает на вход изображение с двумя зелеными квадратами
    # и возвращает обрезанное по ним
    f = open("OpenCV Skolkovo/settins.txt", "r")
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
    cv.imwrite("OpenCV Skolkovo/45.png", mask1)
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


def circle_cw(img):  # Функция нахождения центра самого большого желтого элепса на картинке, принимает на вход картинку.
    # Возвращает координаты центра элепса
    clone = img.copy()
    hsv = cv.cvtColor(clone, cv.COLOR_BGR2HSV)  # переводим изображение в цветовое пространство HSV

    f = open("OpenCV Skolkovo/settins.txt", "r")
    try:
        min_max = list(map(int, f.readlines()[4].split(" ")))
    except ValueError:
        print("Предыдущие этапы настройки завершены неправильно, переделайте их")
        return

    bilateral_filtered_image = cv.inRange(hsv, (min_max[0], min_max[1], min_max[2]),
                                          (min_max[3], min_max[4], min_max[5]))
    # Биноризуем по порогам (минимальный - 2 аргумент, максимальный - 3, HSV - соответственно)

    # edge_detected_image = cv.Canny(bilateral_filtered_image, 75, 200)

    contours, _ = cv.findContours(bilateral_filtered_image, cv.RETR_TREE,
                                  cv.CHAIN_APPROX_SIMPLE)  # ищем конутры на бинорезованнном изображении
    contours = sorted(contours, key=cv.contourArea, reverse=True)  # сортируем их по площади

    ellipse = cv.fitEllipse(contours[0])  # На замом большом контуре вписываем элепс
    el = ellipse
    # cv.ellipse(clone,ellipse,(0,0,255),2)

    el = list(el)  # Переводим в изменяемый список
    el[0] = list(el[0])
    el[1] = list(el[1])

    x = el[0][0]  # вытаскиваем координаты элепса
    y = el[0][1]
    # el[1][0] = 2
    # el[1][1] = 2
    # el[2] = 2
    # el[0] = tuple(el[0])
    # el[1] = tuple(el[1])
    # el = tuple(el)
    # cv.ellipse(clone, el, (255, 0, 0), 3)
    return [x, y]  # возвращаем координаты в виде списка


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


def volt_(pos_circle, bg_v):
    f = open("OpenCV Skolkovo/settins.txt", "r")
    sp = f.readlines()[3]
    sp = sp.split("QQQ")
    for i in range(len(sp)):
        sp[i] = sp[i].split("XXX")
        for j in range(len(sp[i])):
            sp[i][j] = sp[i][j].split(" ")
            for x in range(len(sp[i][j])):
                sp[i][j][x] = int(sp[i][j][x])

    res = bs(sp, pos_circle[0])

    if res == 0:
        for i in range(1, 100):
            res = bs(sp, pos_circle[0] + i)
            if res != 0:
                return res + bg_v
    else:
        return res + bg_v


def inPolygon(x, y, xp, yp):
    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= y < yp[i - 1]) or (yp[i - 1] <= y < yp[i])) and
                (x > (xp[i - 1] - xp[i]) * (y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
            c = 1 - c
    return c

# img = cv.imread('3.png')
# # img = scale_img(img, 1000)
# # cv.imwrite('1.png', img)
# # cv.imshow("ImG", img)
# # cv.waitKey(0)

# cam = cv.VideoCapture(1)
#
# while True:
#     _, frame = cam.read()
#     c = cutting_img(frame)
#     print(volt(c, [250, 20]))
#     cv.imshow("", c)
#
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break
