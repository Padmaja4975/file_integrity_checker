# File Integrity Checker

A Python tool that monitors files in a directory for unauthorized changes using SHA-256 hashing.

## Features
- Creates a baseline of SHA-256 hashes for all files in a directory
- Detects new files, modified files, and deleted files by comparing against the baseline
- Simple menu-driven CLI

## Tech Stack
- Python 3
- Libraries: hashlib, os, json

## How to Run
1. Run `python file_integrity_checker.py`
2. Choose option 1 to create a baseline (first time)
3. Run again with option 2 to check for changes against the baseline

## Project Context
Built during the Cybersecurity & Ethical Hacking internship at CodTech IT Solutions.
