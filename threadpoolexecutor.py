from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

URLS = ["https://httpbin.org/delay/2", "https://httpbin.org/delay/1", "https://httpbin.org/get"]

def fetch(url):
    return url, requests.get(url, timeout=5).status_code

with ThreadPoolExecutor(max_workers=10) as pool:
    futures = [pool.submit(fetch, u) for u in URLS]
    for fut in as_completed(futures):
        url, status = fut.result()
        print(url, status)