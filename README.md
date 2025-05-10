# passStrengthchecker

A Python program to validate and check the strength of passwords based on specific criteria such as length, uppercase, lowercase, digits, and special characters.

## Features
- **Checks if the password contains both uppercase and lowercase letters**.
- **Checks for at least one numeric digit**.
- **Validates the presence of special characters** like `!@#$%^&*()_+{}[]?<>.,;':=`.
- **Determines if the password is weak, medium, or strong** based on the following criteria:
    - **Weak**: Less than 8 characters.
    - **Medium**: Missing at least one category (lowercase, uppercase, digit, or special character).
    - **Strong**: Meets all the criteria (length >= 8, includes lowercase, uppercase, digits, and special characters).

## Requirements
- Python 3.x
- `unittest` module for testing (built-in with Python)

## Installation
1. Clone or download this repository.
2. Make sure you have Python 3.x installed on your machine.
3. No additional dependencies are required.

## Usage
To use the password checker, follow the steps below:

1. Import the `DetectPassword` class:
    ```python
    from passwordDetection import DetectPassword
    ```

2. Create an instance of the `DetectPassword` class and call the `strong_password_detection` method with a password:
    ```python
    dp = DetectPassword()
    result = dp.strong_password_detection("YourPasswordHere")
    print(result)
    ```

## Testing

To test the program, the `unittest` module is used. The `TestDetectPassword` class contains test cases for weak, medium, and strong passwords.

### Running Tests
To run the tests, use the following command:

```bash
python -m unittest test_password_checker.py
dp = DetectPassword()
print(dp.strong_password_detection("TestPass#456"))

(TestPass#456) PASSWORD STATUS: STRONG - VALID PASSWORD

dp = DetectPassword()
print(dp.strong_password_detection("abc"))

(abc) PASSWORD STATUS: WEAK - must be at least 8 characters long.



