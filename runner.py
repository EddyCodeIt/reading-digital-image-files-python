import labels_reader


train_labels = 'data/train-labels-idx1-ubyte.gz'
test_labels = 'data/t10k-labels-idx1-ubyte.gz'
labels_reader.read_label_training_sets(train_labels)