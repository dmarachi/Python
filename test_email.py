import unittest
import email1

class emailTests(unittest.TestCase):

	def test_email_method(self):
		self.assertEqual(email1.email("larry", "shumlich"), "larry.shumlich@evolveu.ca")
		self.assertEqual(email1.email("dima", "marachi"), "dima.marachi@evolveu.ca")

	# def test_email_method():
	# 	assert my_email("larry", "shumlich") == "larry.shumlich@evolveu.ca"
	# 	assert my_email("heiko", "peters") == "heiko.peters@evolveu.ca"

    
if __name__ == "__main__":
	unittest.main()
