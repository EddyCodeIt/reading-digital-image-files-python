import gzip, numpy

def read_image_files(filepath):
    with gzip.open(filepath, "rb") as image_file:

        # Read magic number of file represented by first 4 bytes
        magicNum = int.from_bytes(image_file.read(4), 'big')  
        print("Magic number: ", magicNum)

        # Read number of images in the file

        num_img = int.from_bytes(image_file.read(4), 'big')
        print("Number of images in a file: ", num_img)

        # Data set file also contains information about dimensions 
        # of an images represented in numbers for rows and columns.
        # Dimensions of images in MNIST data set is 28x28
        
        num_rows = int.from_bytes(image_file.read(4), 'big')
        num_cols = int.from_bytes(image_file.read(4), 'big')
        print("Rows: ", num_rows, " | Columns: ", num_cols)

        images = [] # Array to store images. 
                    # Each index holds array of rows corresponding to a particular image 
                    # Each index in array of rows holds array of columns that is correspondant 
                    # to that image. 

        for i in range(num_img):
            rows = []
            for r in range(num_rows):
                cols = []
                for c in range(num_cols):
                    cols.append(int.from_bytes(image_file.read(1), 'big'))
                rows.append(cols)
            images.append(rows)

    return images


# print(len(read_image_files('data/train-images-idx3-ubyte.gz'))) # for testing
