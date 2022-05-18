from skimage import io,data
import matplotlib.pyplot as plt
import numpy as np

img = data.coffee()
print(img.shape)
print(type(img))
ratio = 10
image1 = np.zeros((int(img.shape[0]//ratio),
                   int(img.shape[1]//ratio),
                   img.shape[2]), dtype='int32')

for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in  range(image1.shape[2]):
            delta = img[i*ratio:(i+1)*ratio, j*ratio:(j+1)*ratio, k]
            image1[i,j,k]=np.mean(delta)
plt.imshow(image1)
plt.show()
# io.imshow(img)  # 显示图片
#io.imsave('test1.jpg', img) # 保存图片
plt.show()
if __name__ == '__main__':
    print("start")
