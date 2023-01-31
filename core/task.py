from celery import shared_task
from core.models import *
import  csv, os
import numpy as np
import pandas as pd

@shared_task
def generate_file(filename, no_of_rows): 
    try:
        os.makedirs("data", exist_ok=True) 
        with open(f'data/{filename}', 'w', encoding='UTF8', newline='') as f:
            for i in range(0, no_of_rows):
                writer = csv.writer(f)
                writer.writerow([i])
        print("Done.")
    except Exception as e:
        print (e)

# csv using pandas and numpy
@shared_task
def generate_file2(filename, no_of_rows): 
    try:
        os.makedirs("data", exist_ok=True) 
        df = pd.DataFrame(np.random.randn(no_of_rows, 3), columns=list('ABC'))
        df.to_csv(f'data/{filename}', index=False)
    except Exception as e:
        print(e)
