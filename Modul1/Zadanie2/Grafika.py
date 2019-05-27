from PIL import Image
import numpy as np

class Grafika:
    def __init__(self,filePath):
        self.filePath = filePath
        imageFile = Image.open(self.filePath)
        self.width,self.height = imageFile.size
        self.red = [[] for _ in range(self.width)]
        self.green = [[] for _ in range(self.width)]
        self.blue = [[] for _ in range(self.width)]
       

    def MACIERZ(self):
        imageFile = Image.open(self.filePath)
        for y in range(self.height):
            for x in range(self.width):
               
                r,g,b,a = imageFile.getpixel((x,y))
                self.red[y].append(r)
                self.green[y].append(g)
                self.blue[y].append(b)
    def filter(self,filterName = "blur"):
        
        box_kernel = [[1 / 9, 1 / 9, 1 / 9],
                    [1 / 9, 1 / 9, 1 / 9],
                    [1 / 9, 1 / 9, 1 / 9]]

       
        gaussian_kernel = [[1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256],
                        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                        [6 / 256, 24 / 256, 36 / 256, 24 / 256, 6 / 256],
                        [4 / 256, 16 / 256, 24 / 256, 16 / 256, 4 / 256],
                        [1 / 256, 4  / 256,  6 / 256,  4 / 256, 1 / 256]]
        sharp_kernel = [[  0  , -.5 ,    0 ],
          [-.5 ,   3  , -.5 ],
          [  0  , -.5 ,    0 ]]
        if filterName is "blur":
            kernel = box_kernel
        elif filterName is "Gauss":
            kernel = gaussian_kernel
        elif filterName is "sharp":
            kernel = sharp_kernel

        
        offset = len(kernel) // 2

        
        
        rgbArray =np.zeros((self.height,self.width,3), 'uint8')

        
        for y in range(offset, self.width - offset):
            for x in range(offset, self.height - offset):
                acc = [0, 0, 0]
                for a in range(len(kernel)):
                    for b in range(len(kernel)):
                        xn = x + a - offset
                        yn = y + b - offset
                        
                        acc[0] += self.red[xn][yn] * kernel[a][b]
                        acc[1] += self.green[xn][yn] * kernel[a][b]
                        acc[2] += self.blue[xn][yn] * kernel[a][b]
                rgbArray[x][y][0] = acc[0]
                rgbArray[x][y][1] = acc[1]
                rgbArray[x][y][2] = acc[2]
        img = Image.fromarray(rgbArray)
        img.save(self.filePath + "_"+filterName+'.jpeg')
   
g = Grafika("python.jpg")
g.MACIERZ()
g.filter()
g.filter("Gauss")
g.filter("sharp")


