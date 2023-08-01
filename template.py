import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d  %H%M%S')

project_name='textSummarizer'

list_of_files = [
    'main.py',
    
    'requirements.txt',
    'setup.py',
    
    
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating Directory:{filedir} for the file {filename}')

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists.')