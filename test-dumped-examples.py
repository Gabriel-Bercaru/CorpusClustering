from itertools import chain
import os
import pickle

BASE_DATASET = 'DataSet-Lite'
UNCOMPRESSED_BINS_PATH = 'bins-uncompressed'
COMPRESSED_BINS_PATH = 'bins-compressed'

REPORT_FREQ =  10

def count_examples_in_dir(dir_path):
    num_examples = 0
    
    files = os.listdir(dir_path)
    files.sort()
    
    for idx_file, file in enumerate(files):
        if idx_file % REPORT_FREQ == 0:
            print('Loading file {}/{} [{:.2f}%]'.format(idx_file + 1, len(files), (idx_file + 1) / len(files) * 100.))
        full_path = os.path.join(dir_path, file)
        f = open(full_path, 'rb')
        data = pickle.load(f)
        num_examples += len(data)
    
    return num_examples

def main():
    full_uncompressed_path = os.path.join(BASE_DATASET, UNCOMPRESSED_BINS_PATH)
    full_compressed_path = os.path.join(BASE_DATASET, COMPRESSED_BINS_PATH)
    
    num_examples_uncompressed = count_examples_in_dir(full_uncompressed_path)
    num_examples_compressed = count_examples_in_dir(full_compressed_path)
    
    print('Number of examples in uncompressed bins directory: {}'.format(num_examples_uncompressed))
    print('Number of examples in compressed bins directory: {}'.format(num_examples_compressed))
    
if __name__ == '__main__':
    main()