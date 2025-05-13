# 🛡️ Python Account Management System & Password Strength Checker

This repository contains two Python-based projects:

1. **Account Management System** – A command-line interface for user registration and login with email/password validation.
2. **Password Strength Checker** – A Python class to validate password strength using specific criteria.

---

## 🔐 1. Account Management System

A simple CLI-based system that allows users to **register**, **login**, and manage account details with local file-based storage.

### 🚀 Features

- Unique username generation
- Email format validation
- Strong password enforcement (via `DetectPassword` class)
- Optional middle name during registration
- Retry mechanism for login attempts
- "Forgot Password" feature
- Account info stored as `.txt` files in the `Accounts/` folder

### 📁 Folder Structure


---

## 🔑 2. Password Strength Checker

A utility to validate and rate the strength of passwords.

### ✅ Criteria

- **Minimum 8 characters**
- **At least one uppercase and one lowercase letter**
- **At least one digit**
- **At least one special character** (`!@#$%^&*()_+{}[]?<>.,;':=`)

### 🔍 Strength Levels

- **Weak**: Less than 8 characters  
- **Medium**: Missing one or more required character types  
- **Strong**: Meets all requirements  

### 🧪 Testing

Includes a `unittest` test suite to validate password strength across different cases.

### 📦 How to Use

```python
from passwordDetection import DetectPassword

dp = DetectPassword()
print(dp.strong_password_detection("TestPass#456"))
# Output: (TestPass#456) PASSWORD STATUS: STRONG - VALID PASSWORD
## 📋 Requirements

- Python 3.x  
- `unittest` (built-in with Python)

## 📌 Notes

- This is a beginner-friendly project for learning file handling, validation, and OOP in Python.
- For production use, consider securing stored passwords (e.g., hashing with `bcrypt`).
