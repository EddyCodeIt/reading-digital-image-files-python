import gzip, struct

myFile = gzip.open('data/t10k-images-idx3-ubyte.gz','rb')
# pointer position starts at start.
# everytime .read() function is called, pointer possition 
# stays where .read() stoped. 
magicNum = myFile.read(4)

#  firstbyte var would print as: b'\x00\x00\x08\x03'
# In binary, this is: 00000000 00000000 00000100 00000011

print(type(magicNum))
print(magicNum)

print("Magic Number: ",int.from_bytes(magicNum, 'big'))

# each image is 28 by 28 bytes, 10 000 images in a file + bytes for meta date about a file
# print(28*28*10000+4+4+4+4)

no_lbl = myFile.read(4)
no_lbl = int.from_bytes(no_lbl, 'big')
print("Number of labels: ", no_lbl)

labels = [myFile.read(1) for i in range(no_lbl)]
labels = [int.from_bytes(label, 'big') for label in labels]

print(labels)