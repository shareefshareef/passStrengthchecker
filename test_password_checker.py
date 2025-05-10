
import unittest
from passwordDetection import DetectPassword  

class TestDetectPassword(unittest.TestCase):

    def setUp(self):
        '''Setup method that runs before each test'''
        self.dp = DetectPassword()

    def test_weak_passwords(self):
        '''Test weak passwords'''
        weak_passwords = [
            "abc",
            "1234567",
            "ABC",
            "aB3!",
            "xyz123",
        ]
        for pwd in weak_passwords:
            with self.subTest(pwd=pwd):
                result = self.dp.strong_password_detection(pwd)
                self.assertIn("WEAK", result)

    def test_medium_passwords(self):
        '''Test medium passwords'''
        medium_passwords = [
            "onlylowercase",
            "ONLYUPPERCASE",   
            "MixCaseOnly",     
            "Pass1234",     
            "NoDigits@",  
            "Test@Case",  
        ]
        for pwd in medium_passwords:
            with self.subTest(pwd=pwd):
                result = self.dp.strong_password_detection(pwd)
                self.assertIn("MEDIUM", result)

    def test_strong_passwords(self):
        '''Test strong passwords'''
        strong_passwords = [
            "Strong@123",
            "TestPass#456",
            "Abc@2024!",
            "My_Pass9$",
            "Secure#99",
            "Welcome#1",
            "Xyz@890Z"
        ]
        for pwd in strong_passwords:
            with self.subTest(pwd=pwd):
                result = self.dp.strong_password_detection(pwd)
                self.assertIn("STRONG", result)


if __name__ == "__main__":
    unittest.main()

