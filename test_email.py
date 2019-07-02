import unittest
import email

class emailTests(unittest.TestCase):

	def test_email_method(self):
		self.assertEqual(email.email("larry", "shumlich"), "larry.shumlich@evolveu.ca")

	def test_email_method():
    assert my_email("larry", "shumlich") == "larry.shumlich@evolveu.ca"
    assert my_email("heiko", "peters") == "heiko.peters@evolveu.ca"

    
if __name__ == "__main__":
	unittest.main()