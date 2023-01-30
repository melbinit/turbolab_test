from celery import shared_task
from core.models import *
import  csv, os

@shared_task
def generate_file(filename, no_of_rows): 
    os.makedirs("data", exist_ok=True) 
    with open(f'data/{filename}', 'w', encoding='UTF8', newline='') as f:
        for i in range(0, no_of_rows):
            writer = csv.writer(f)
            writer.writerow([i])
    print("Done.")