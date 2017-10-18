import numpy
import PIL.Image as pilImg

# function that does image saving 
def save_img(img, label, position, set_type):
    
    img = img.convert('RGB')
    # building name for the file
    img_name = set_type + "-" + '{:05}'.format(position) + "-" + str(label) + ".png"

    img.save(set_type + "_imgs/" + img_name)


# function that itterates over passed in arrays 
# and save image for each item in those arrays
def load_data(img_arr, label_arr, set_type):

    print("Exporting images to PNG file...")
    ctr = 1 # tracks itteration count to append it to a file name

    # zip() funtion allows to itterate over few arrays sequentially
    # it stops whenever one of the arrays has no items left to 
    # itterate over. It is handy in this particular scenario,
    # since we know both arrays have equal number of elements in them.
    for i, l in zip(img_arr, label_arr) :
        img = pilImg.fromarray(numpy.array(i)) # 
        save_img(img, l, ctr, set_type)
        ctr += 1
    

