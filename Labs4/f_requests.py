import requests

def get_status(url):
    try:
        return requests.get(url, timeout=5).status_code
    except requests.RequestException:
        return None