from unittest import TestCase
from monitor import WebsiteMonitor
import unittest


class TestWebsiteMonitor(TestCase):
    def test_check_website_status(self):
        ## TC1: Website is online ; returns a statuscode
        self.assertEqual(200, WebsiteMonitor.check_website_status('https://hilko.eu'))
        self.assertEqual(500, WebsiteMonitor.check_website_status('http://httpstat.us/500'))
        

        ## TC2: Website is online ; redirects
        self.assertEqual(200, WebsiteMonitor.check_website_status('http://httpstat.us/301'))
        self.assertEqual(301, WebsiteMonitor.check_website_status('http://httpstat.us/301', follow_redirects=False))


        ## TC3: Server is not reachable (i.e. no DNS entry or server offline)
        self.assertEqual(None, WebsiteMonitor.check_website_status('https://xaxaxaxaxa.hilko.eu'))

        ## TC4: Counter-Test
        self.assertNotEqual(200, WebsiteMonitor.check_website_status('http://httpstat.us/404'))
        

if __name__ == '__main__':
    unittest.main()