from run import app
import unittest
import requests

import os


class ApiUnitTest(unittest.TestCase):
    API_URI = 'http://127.0.0.1:5000'

    # Ensure flask api is Listening
    def test_1_get_all_index_redirect(self):
        tester = app.test_client(self)
        r = tester.get(ApiUnitTest.API_URI, content_type='html/text')
        self.assertEqual(r.status_code, 308)

    # Ensure Api is listenig at allContacts
    def test_2_get_all_contacts(self):
        tester = app.test_client(self)
        r = tester.get(f"{ApiUnitTest.API_URI}/contacts", content_type='html/text')
        self.assertEqual(r.status_code, 200)

    # Ensure Api is listenig at search
    def test_3_get_contact_from_search(self):
        tester = app.test_client(self)
        r = tester.post(f"{ApiUnitTest.API_URI}/search", data={'search': 'Arer'})
        self.assertEqual(r.status_code, 200)

    # # Ensure Api is listenig at contact/delete and delete contact
    def test_4_delete_contact(self):
        tester = app.test_client(self)
        r = tester.post(f"{ApiUnitTest.API_URI}/contacts/delete", data={'id': '1'})
        self.assertEqual(r.status_code, 302)

    # # Ensure Api is listenig at edit_contact
    def test_5_edit_contact(self):
        tester = app.test_client(self)
        r = tester.post(f"{ApiUnitTest.API_URI}/edit_contact/1", data={})
        self.assertEqual(r.status_code, 200)

    # # Ensure Api is listenig at allContacts
    def test_2_get_all_contacts(self):
        tester = app.test_client(self)
        r = tester.get(f"{ApiUnitTest.API_URI}/contacts", content_type='html/text')
        self.assertEqual(r.status_code, 200)

    # # Ensure Api is listenig at allContacts
    def test_2_get_create_contacts(self):
        tester = app.test_client(self)
        r = tester.get(f"{ApiUnitTest.API_URI}/contacts", data={'name': "bhanu", 'email': 'Pbhanu@gmail.com', 'phone_number': "1234567890"} content_type='html/text')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main(exit=False)
