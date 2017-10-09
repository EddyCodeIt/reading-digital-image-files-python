import labels_reader, images_reader, image_saver


train_labels = 'data/train-labels-idx1-ubyte.gz'
test_labels = 'data/t10k-labels-idx1-ubyte.gz'

train_images = 'data/train-images-idx3-ubyte.gz'
test_images = 'data/t10k-images-idx3-ubyte.gz'

labels_arr = labels_reader.read_label_files(train_labels)
print()
images_arr = images_reader.read_image_files(train_images)

image_saver.load_data(images_arr , labels_arr, "test")


