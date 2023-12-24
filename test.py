import unittest
import warnings
from company import app as Company
from sales import app


class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def get_other_company_details(self):
        response = self.app.get("/company/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual("Chain store offering pet food, accessories, and grooming services" in response.data.decode())

    def test_getcompany(self):
        response = self.app.get("/company")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Green Valley Groceries" in response.data.decode())

    def test_getcompany_by_id(self):
        response = self.app.get("/company/10")  
        self.assertEqual(response.status_code, 200)
        self.assertTrue("10" in response.data.decode())

    def test_getsales(self):
        response = self.app.get("/sales")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("129.99" in response.data.decode())


if __name__ == "__main__":
    unittest.main()
