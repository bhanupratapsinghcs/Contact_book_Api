from run import app
import unittest
import requests

import os


class ApiUnitTest(unittest.TestCase):
    API_URI = 'http://127.0.0.1:5000'
    search_data = {'search': 'Arer'}

    # Ensure flask api is Listening
    def test_1_get_all_redirect(self):
        tester = app.test_client(self)
        r = tester.get(ApiUnitTest.API_URI, content_type='html/text')
        self.assertEqual(r.status_code, 308)

    # Ensure Api is listenig at allContacts
    def test_2_get_all_contacts(self):
        tester = app.test_client(self)
        r = tester.get(f"{ApiUnitTest.API_URI}/contacts", content_type='html/text')
        self.assertEqual(r.status_code, 200)

    # Ensure Api is listenig at search
    def test_2_get_contact_from_search(self):
        tester = app.test_client(self)
        r = tester.post(f"{ApiUnitTest.API_URI}/search", form=[('search',"Arer")])
        self.assertEqual(r.status_code, 200)

    # # Ensure Api is listenig at allContacts
    # def test_2_get_all_contacts(self):
    #     tester = app.test_client(self)
    #     r = tester.get(f"{ApiUnitTest.API_URI}/contacts", content_type='html/text')
    #     self.assertEqual(r.status_code, 200)

    # # Ensure Api is listenig at allContacts
    # def test_2_get_all_contacts(self):
    #     tester = app.test_client(self)
    #     r = tester.get(f"{ApiUnitTest.API_URI}/contacts", content_type='html/text')
    #     self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main(exit=False)
