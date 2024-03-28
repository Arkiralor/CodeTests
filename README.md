# Code Tests

This repository holds code that is used primarilly to test-out `production`-grade snippets.

## Contents

1. __[001](src/001.py):__ This code snippet is used to retrive a secret from AWS Secrets Manager and then export the secret to the executing machine's environment.

## Setup

### Pre-Requisites

1. Python v3.10
2. Bash
    - GitBash for Windows

### Step-by-Step Instructions

1. `python -m venv env` to generate a virtual environment for python.
2. `source env/bin/activate` to activate the virtual environment that was just created.
    - `source env/Scripts/activate` on windows.