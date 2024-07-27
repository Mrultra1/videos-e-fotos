import os
import cv2

path = "imagens/"
images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext.lower() in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path + "/" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(count):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Concluído")
