import os
import pickle
import numpy as np

UNCOMPRESSED_DIR = 'bins-uncompressed/'

def main():
    all_files = os.listdir(UNCOMPRESSED_DIR)
    all_files.sort()
    
    for idx, file in enumerate(all_files):
        full_old_path = os.path.join(UNCOMPRESSED_DIR, file)
        #crt_file_tokens = file.split('-')
        
        '''
        first_non_shard_token_idx = -1
        for i in range(len(crt_file_tokens)):
            if 'bin' in crt_file_tokens:
                first_non_shard_token_idx = i
                break
        '''
        
        #remaining_tokens = crt_file_tokens[first_non_shard_token_idx - 2:]
        #new_file_path = '-'.join(remaining_tokens)
        new_file_path = 'shard-0000-' + file
        full_new_path = os.path.join(UNCOMPRESSED_DIR, new_file_path)
        
        #print('Renaming {} ----- {}'.format(full_old_path, full_new_path))
        os.rename(full_old_path, full_new_path)

if __name__ == '__main__':
    main()