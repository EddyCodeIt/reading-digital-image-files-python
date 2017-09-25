import gzip, struct, numpy
import PIL.Image as pilImg


# pointer position starts at start.
# everytime .read() function is called, pointer possition 
# stays where .read() stoped. 

def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as myFile:

        magicNum = myFile.read(4)

        #  firstbyte var would print as: b'\x00\x00\x08\x03'
        # In binary, this is: 00000000 00000000 00000100 00000011

        print(type(magicNum))
        print(magicNum)

        print("Magic Number: ",int.from_bytes(magicNum, 'big'))

        no_lbl = myFile.read(4) # read how many labels in the file 
        no_lbl = int.from_bytes(no_lbl, 'big') # convert from bytes into ints
        print("Number of labels: ", no_lbl)

        labels = [myFile.read(1) for i in range(no_lbl)] # read labels byte by byte
        labels = [int.from_bytes(label, 'big') for label in labels] # convert into ints

    return labels

train_labels = read_labels_from_file('data/train-labels-idx1-ubyte.gz')
test_labels = read_labels_from_file('data/t10k-labels-idx1-ubyte.gz')


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