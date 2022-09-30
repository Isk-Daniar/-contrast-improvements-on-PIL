from PIL import Image
import numpy as np

img = Image.open('lunar03_raw.jpg')
data = np.array(img)
min = np.min(data)
max = np.max(data)
a = 255 / (max - min)
b = 255 - max * a

x, y = data.shape
update_date = np.zeros((x, y))
for i in range(x):
    for j in range(y):
        update_date[i][j] = a * data[i][j] + b

res_img = Image.fromarray(update_date)
if res_img.mode != 'RGB':
    res_img = res_img.convert("RGB")

img.show()
res_img.show()
res_img.save('new_lunar03_raw.jpg')