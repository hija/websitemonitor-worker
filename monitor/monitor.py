import requests


class WebsiteMonitor:
    """
    Monitors a website
    """

    @staticmethod
    def check_website_status(website: str, follow_redirects=True) -> int:
        """Return the status code of a website.

        Args:
            website (str): Websiteurl as string.
            follow_redirects (bool, optional):
                Whether redirects should be followed or not. Defaults to True.

        Returns:
            Int: HTTP-Statuscode, -1 bei Fehler
        """
        try:
            response = requests.get(
                website, timeout=1, allow_redirects=follow_redirects)
            return int(response.status_code)
        except (requests.HTTPError,
                requests.Timeout,
                requests.ConnectionError):
            return -1
