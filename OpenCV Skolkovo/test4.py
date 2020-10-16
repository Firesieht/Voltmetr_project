import cv2 as cv


def scale_img(frame, scale_percent):  # функция, для изменения размера изображения.
    # Принимает два аргумента scale_img( изображение в виде numpy массива, процент уменшения изображения))
    width = int(frame.shape[1] * scale_percent / 100)  # записываем в перемнные уменьшенные ширину и высоту
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)  # записываем их в tuple
    frame = cv.resize(frame, dim, interpolation=cv.INTER_AREA)  # уменьшаем по заданным параметрам
    return frame  # возвращаем уменьшенное изображение


cam = cv.VideoCapture(0)

while True:
    _, frame = cam.read()
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break