import requests
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from rich.progress import Progress
from .utils import extract_title, verify_admin_panel

class AdminScanner:
    def __init__(self, target, threads=50, timeout=10):
        self.target = target
        self.threads = threads
        self.timeout = timeout
        self.results = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def scan_url(self, path):
        url = f"{self.target.rstrip('/')}/{path.lstrip('/')}"
        try:
            response = requests.get(
                url,
                headers=self.headers,
                timeout=self.timeout,
                verify=False,
                allow_redirects=True
            )
            if response.status_code in [200, 201, 202, 301, 302]:
                if verify_admin_panel(response):
                    return {
                        'url': url,
                        'status': response.status_code,
                        'length': len(response.content),
                        'title': extract_title(response.text)
                    }
        except:
            pass
        return None

    def start_scan(self, paths):
        with Progress() as progress:
            task = progress.add_task("[cyan]Scanning...", total=len(paths))
            
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                future_to_url = {
                    executor.submit(self.scan_url, path): path 
                    for path in paths
                }
                
                for future in concurrent.futures.as_completed(future_to_url):
                    result = future.result()
                    if result:
                        self.results.append(result)
                    progress.update(task, advance=1)
