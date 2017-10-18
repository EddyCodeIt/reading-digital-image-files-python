# MNIST data sets lab

GMIT Software Development Module Emerging Technologies
Original lab problems can be found [here](https://emerging-technologies.github.io/problems/mnist.html) 

In this lab I am demonstraiting how I use Python to read MNIST data sets and ability to interprit it in some other format, be it a string representation of data to console or a data output to a file e.g., `.png`.

MNIST data sets can be found [here]()

## Core objectives of the lab were:

* Unzip data set files, read data from a byte stream and place it into appropriate data structures.

* Study, split and output values from this data structures into meaningful form i.e., convert collection of bytes into an image this bytes represent.

*  Learn new Python techniques and practices used in everyday programming e.g., use of common libraries, separation of modular concerns... 


## Components

* runner.py - an entry point to an application. This is the file to run with compiler. It provides a user with a menu to operate application functions. 

* labels_reader.py - module that is responsible for reading labels data sets and returning a list of labels. Each label digit corresponds to a number represented in the image file of the image data set. Those labels are later used to name an image files.
                       
* images_reader.py - this module reads data sets that store bytes of images and constructs a more complecated data structures of nested lists to be used later. 

* image_saver.py - module with a methods to handle saving of each individual image from a data structure of bytes to a file, giving it appropriate name and file extension. 

