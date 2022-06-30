import os
from PIL import Image

path = 'original folder path'
resultPath = 'result folder path'

if not os.path.exists(resultPath):
    os.mkdir(resultPath)

list = os.listdir(path)

list.sort()
for filename in list:
    file = path + filename

    img = Image.open(file)
    img = img.convert('RGB')
    img.save(os.path.join(resultPath, filename), 'jpeg', qualty=60)