import time
from tqdm import tqdm

def progress(n=20):
    for _ in tqdm(range(n), desc="Працюю"):
        time.sleep(0.05)