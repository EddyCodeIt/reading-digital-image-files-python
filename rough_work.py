import gzip, numpy
import PIL.Image as pilImg


def read_images_from_file(filename):
    with gzip.open(filename,'rb') as myFile:
        magicNum = myFile.read(4)
        print("Magic Number: ",int.from_bytes(magicNum, 'big'))

        noimg = myFile.read(4)
        noimg = int.from_bytes(noimg, 'big') 
        print("Number of images: ", noimg)

        norow = myFile.read(4)
        norow = int.from_bytes(norow, 'big') 
        print("Number of rows: ", norow)

        nocol = myFile.read(4)
        nocol = int.from_bytes(nocol, 'big') 
        print("Number of columns: ", nocol)
        
        images = []

        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(myFile.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

train_images = read_images_from_file('data/train-images-idx3-ubyte.gz')
# test_images = read_images_from_file('data/t10k-images-idx3-ubyte.gz')


for row in train_images[4999]:
    for col in row:
        print('.' if col <= 128 else '#', end = '') 
    print()

img = pilImg.fromarray(numpy.array(train_images[4999]))
img = img.convert('RGB')
img.show()
img.save('2.png')   