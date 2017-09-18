import gzip, struct

myFile = gzip.open('data/t10k-images-idx3-ubyte.gz','rb')

magicNum = myFile.read(4)

#  firstbyte var would print as: b'\x00\x00\x08\x03'
# In binary, this is: 00000000 00000000 00000100 00000011

print(type(magicNum))
print(magicNum)

print(int.from_bytes(magicNum, byteorder ='big'))

# each image is 28 by 28 bytes, 10 000 images in a file + bytes for meta date about a file
print(28*28*10000+4+4+4+4)