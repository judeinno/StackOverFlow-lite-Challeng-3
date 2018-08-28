import unittest
import json
from app.tests.Basetest import BaseTest


class TestClass(BaseTest):

    def test_user_siginup(self):
        """Test API can signup """

        res = self.client().post('/api/v1/auth/signup',
                                 content_type='application/json',
                                 data=json.dumps(self.user_reg))
        self.assertTrue(res.status_code, 201)
        self.assertIn('User successfully registered', str(res.data))


if __name__ == '__main__':
    unittest.main()