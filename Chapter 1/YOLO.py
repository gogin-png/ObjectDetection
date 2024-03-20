import cv2
from ultralytics import YOLO


# Создается экземпляр модели Chapter 1, загружая предобученную модель из файла 'yolov8n.pt' (можно указать путь для скачки).
model = YOLO('/home/denis/PycharmProjects/ObjectDetection/YoloModels/yolov8n.pt')

# Модель используется для обнаружения объектов на изображении, указанном в пути ' Результаты обнаружения сохраняются в переменной results.
results = model("/home/denis/PycharmProjects/ObjectDetection/images/1.jpg",show=True)

# Ожидается нажатие клавиши (любой) для продолжения выполнения программы после отображения результатов обнаружения на изображении.
cv2.waitKey(0)