from PIL import Image, ImageOps
import numpy

chars = ['@', '&', 'J', '8', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ', ' ']
charsInverted = [' ', ' ', '.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '8', 'J', '&', '#']
WIDTH = 100
HEIGHT = 100

image = Image.open('image5.jpg', 'r')

WIDTH, HEIGHT = image.size
WIDTH = int(WIDTH / 2.5)
HEIGHT = int(HEIGHT / 2.5)

imageG = ImageOps.grayscale(image)
image2 = imageG.resize((WIDTH, HEIGHT))
#image.show()

array = numpy.asarray(image2)
#print(array)

def getChar(num):
    if num >= 0 and num <= 15:
        return chars[0]
    if num >= 15 and num <= 30:
        return chars[1]
    if num >= 30 and num <= 45:
        return chars[2]
    if num >= 45 and num <= 60:
        return chars[3]
    if num >= 60 and num <= 75:
        return chars[4]
    if num >= 75 and num <= 90:
        return chars[5]
    if num >= 90 and num <= 105:
        return chars[6]
    if num >= 105 and num <= 120:
        return chars[7]
    if num >= 120 and num <= 135:
        return chars[8]
    if num >= 135 and num <= 150:
        return chars[9]
    if num >= 150 and num <= 165:
        return chars[10]
    if num >= 165 and num <= 180:
        return chars[11]
    if num >= 180 and num <= 195:
        return chars[12]
    if num >= 195 and num <= 210:
        return chars[13]
    if num >= 210 and num <= 225:
        return chars[14]
    if num >= 225 and num <= 240:
        return chars[15]
    return chars[15]

def getCharInverted(num):
    if num >= 0 and num <= 15:
        return charsInverted[0]
    if num >= 15 and num <= 30:
        return charsInverted[1]
    if num >= 30 and num <= 45:
        return charsInverted[2]
    if num >= 45 and num <= 60:
        return charsInverted[3]
    if num >= 60 and num <= 75:
        return charsInverted[4]
    if num >= 75 and num <= 90:
        return charsInverted[5]
    if num >= 90 and num <= 105:
        return charsInverted[6]
    if num >= 105 and num <= 120:
        return charsInverted[7]
    if num >= 120 and num <= 135:
        return charsInverted[8]
    if num >= 135 and num <= 150:
        return charsInverted[9]
    if num >= 150 and num <= 165:
        return charsInverted[10]
    if num >= 165 and num <= 180:
        return charsInverted[11]
    if num >= 180 and num <= 195:
        return charsInverted[12]
    if num >= 195 and num <= 210:
        return charsInverted[13]
    if num >= 210 and num <= 225:
        return charsInverted[14]
    if num >= 225 and num <= 240:
        return charsInverted[15]
    return charsInverted[15]

for i in range(HEIGHT):
    for j in range(WIDTH):
        #print(getChar(array[i][j]), end=' ')
        print(getCharInverted(array[i][j]), end=' ')
    print("")