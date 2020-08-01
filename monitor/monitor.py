import requests

class WebsiteMonitor:



    @staticmethod
    def check_website_status(website: str, follow_redirects=True):
        try:
            response = requests.get(website, timeout=1, allow_redirects=follow_redirects)
            return int(response.status_code)
        except:
            return None