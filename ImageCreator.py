from PIL import Image

img = Image.open(r'C:\Users\eyesi\PycharmProjects\FileExplorerAnim\Images\Test2.bmp').convert('L')
img = img.convert("L") #grayscale
WIDTH, HEIGHT = img.size


data = list(img.getdata()) # convert image data to a list of integers
#convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

#at this point the image's pixels are all in memory and can be accessed individually using data[row][col]


for row in data:
    for col in data:
        index = data[row][col]
        newimg = Image.new('RGB', (1, 1), color=(index))

#for example:
for row in data:
#    '''print(' '.join('{:3}'.format(value) for value in row))'''
#    print(' '.join('{:3}'.format(value) for value in row))
    newimg = Image.new('RGB', (1, 1), color=())
