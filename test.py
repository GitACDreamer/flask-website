# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-08-03 21:31:49
# @title:  unit test

from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly whit correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='admin', password='sa'), follow_redirects=True)
        self.assertIn(b'You ware logged in!', response.data)

    # Ensure login  behaves correctly with incorect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='admin', password='sa1'), follow_redirects=True)
        self.assertIn(
            b'Invalid credentials. Please try again.', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username='admin',
                                        password='sa'), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were logged out!', response.data)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'You need to login first!', response.data)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to login first!', response.data)

    # Ensure that post show up the main page
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login', data=dict(username='admin', password='sa'), follow_redirects=True)
        self.assertIn(b'Hello from shell.', response.data)


if __name__ == '__main__':
    unittest.main()
