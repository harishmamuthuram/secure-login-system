# secure-login-system

A Python terminal app that implements secure password storage using SHA-256 hashing and salting — no plaintext passwords, ever.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Security](https://img.shields.io/badge/hashing-SHA--256-red)

---

## Features
- Register and log in through the terminal
- Passwords are never stored — only their salted SHA-256 hash is saved
- Unique salt per user means identical passwords produce different hashes
- Account locks after 3 failed login attempts to block brute-force attacks

---

## How it works

1. **Register** — a random salt is generated, combined with your password, and hashed via SHA-256
2. **Login** — the same salt + hash process runs on input and is compared to the stored hash
3. **Lockout** — 3 wrong attempts and the account is locked, no further tries allowed

---

## Requirements

No external libraries — uses Python's built-in `hashlib`.

---

## Usage

```bash
login system with SHA-256 hashing.py
```

---

## ⚠️ Important

- This is a learning project — not production-ready authentication
- Run inside a VM or isolated environment

---

## Built as part of

A self-directed cybersecurity roadmap focused on understanding how real authentication systems protect user data — moving beyond surface-level security knowledge into actual implementation.
