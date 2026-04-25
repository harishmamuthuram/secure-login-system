# Secure Login System (SHA-256)

A Python-based login system that implements secure password storage 
using SHA-256 hashing and salting.

## What it does
Users can register and log in through the terminal. The system locks 
accounts after 3 failed login attempts to prevent brute-force attacks.

## How the security works
Passwords are never stored directly. Instead, each password is combined 
with a unique random salt and passed through SHA-256, producing a fixed 
64-character fingerprint. Even if two users share the same password, 
their stored hashes will differ.

## How to run
1. Clone the repo
2. Run: python login_system.py
3. Choose register or login

## What I learned
Built this to move beyond surface-level security knowledge — implementing 
hashing, salting, and brute-force protection from scratch gave me a 
practical understanding of how real authentication systems protect user data.
