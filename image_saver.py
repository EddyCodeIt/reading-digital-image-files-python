import numpy
import PIL.Image as pilImg

#
def save_img(img, label, position, set_type):
    
    img = img.convert('RGB')
    img_name = set_type + "-" + str(position) + "-" + str(label) + ".png"

    print(img_name)
    

#
def load_data(img_arr, label_arr, set_type):

    ctr = 1

    for i, l in zip(img_arr, label_arr) :
        img = pilImg.fromarray(numpy.array(i))
        save_img(img, l, ctr, set_type)
        ctr += 1
    

