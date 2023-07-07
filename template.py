import os
import sys
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "iot-sensor"

files = [
    '.github/workflows/main.yml',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    
    f'src/{project_name}/utils/__init__.py',
    
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/pipeline/ingestion/__init__.py',
    
    f'src/{project_name}/entity/__init__.py',
    
    f'src/{project_name}/constants/__init__.py',
    
    'data',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/experiments.ipynb',
    '.Dockerfile',
]

for file_path in files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f'Creating Directory: {file_dir} and file: {file_name}')
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            f.write("")
            logging.info(f'Creating Directory: {file_dir} and file: {file_name}')
            
    else:
        logging.info(f'File already exists: {file_path}')
        




