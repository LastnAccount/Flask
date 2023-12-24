import unittest
import warnings
from company import app as Company
from sales import app as Sale
from store import app as Store


class CompanyAppTests(unittest.TestCase):
    def setUp(self):
        Company.config["TESTING"] = True
        self.app = Company.test_client()

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
        
        
class SaleAppTests(unittest.TestCase):
    def setUp(self):
        Sale.config["TESTING"] = True
        self.app = Sale.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)
        
    def test_getsales(self):
        response = self.app.get("/sales")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("129.99" in response.data.decode())
        
    def test_getsales(self):
        response = self.app.get("/sales")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("11" in response.data.decode())
    
    def test_getsales(self):
        response = self.app.get("/sales")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("11" in response.data.decode())
        
        
class StoreppTests(unittest.TestCase):
    def setUp(self):
        Store.config["TESTING"] = True
        self.app = Store.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)
        
    def test_getsales(self):
        response = self.app.get("/stores")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Modern space with co-working space, workshops, and tech demos" in response.data.decode())
        
    def test_getsales(self):
        response = self.app.get("/stores")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Outdoor gear store with expert staff and rental equipment" in response.data.decode())
    
    def test_getsales(self):
        response = self.app.get("/stores")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("789 Elm St, Anytown, USA" in response.data.decode())
        
    def test_getsales(self):
        response = self.app.get("/stores")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Creative Crafts - Craft Corner" in response.data.decode())
        
if __name__ == "__main__":
    unittest.main()
