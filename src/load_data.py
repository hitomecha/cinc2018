import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from logging import StreamHandler, DEBUG, Formatter, FileHandler, getLogger

import physionetchallenge2018_lib as chall

logger = getLogger(__name__)

DIR = 'result_tmp/'

if __name__ == '__main__':

    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s ')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    handler = FileHandler(DIR + 'train.py.log', 'a')
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    logger.info('start')
    
    os.chdir('../input')
    train_files, test_files = chall.get_files()
    
    logger.info('train data : {}'.format(train_files))
    logger.info('test data : {}'.format(test_files))
    logger.info('data load end')

    
    

