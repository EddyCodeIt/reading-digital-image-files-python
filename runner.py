import labels_reader, images_reader, image_saver


train_labels = 'data/train-labels-idx1-ubyte.gz'
test_labels = 'data/t10k-labels-idx1-ubyte.gz'

train_images = 'data/train-images-idx3-ubyte.gz'
test_images = 'data/t10k-images-idx3-ubyte.gz'

print("Enter number for following options: \n1. generate train images\n"
+ "2. generate test images\n3. print number to console screen")
opt = input("Option: ")

if int(opt) == 1:
    print()
    labels_arr = labels_reader.read_label_files(train_labels)
    images_arr = images_reader.read_image_files(train_images)
    image_saver.load_data(images_arr , labels_arr, "train")
    print("Done...")
elif int(opt) == 2:
    print()
    labels_arr = labels_reader.read_label_files(test_labels)
    images_arr = images_reader.read_image_files(test_images)
    image_saver.load_data(images_arr , labels_arr, "test")
    print("Done...")
elif int(opt) == 3:
    print()
    images_arr = images_reader.read_image_files(train_images)

    img = input("Pick an image in range from 1 to 60 000: ")
    
    for row in images_arr[img - 1]:
        for col in row:
            print('.' if col <= 128 else '#', end = '') 
        print()
else:
    print("Invalid input. Exiting...")
    exit()

