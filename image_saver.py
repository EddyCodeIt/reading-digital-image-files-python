import numpy
import PIL.Image as pilImg

#
def save_img(img, label, position, set_type):
    
    img = img.convert('RGB')
    img_name = set_type + "-" + '{:05}'.format(position) + "-" + str(label) + ".png"

    img.save("train_imgs/"+img_name)


#
def load_data(img_arr, label_arr, set_type):

    print("Exporting images to PNG file...")
    ctr = 1

    for i, l in zip(img_arr, label_arr) :
        img = pilImg.fromarray(numpy.array(i))
        save_img(img, l, ctr, set_type)
        ctr += 1
    

