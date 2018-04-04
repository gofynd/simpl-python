
# Simple-Python-Client

**Description**: Simple-Python-Client is a repository which can be used as a python client for Simpl APIs.

## Dependencies
- **Python 3.6**
    Follow the installation section below
- **Mysql 5.7**
    Follow the installation section below
- **Project External Dependancies**
    pip install -r requirements.txt

## Installation
- **Install Python 3.6**:
    https://tecadmin.net/install-python-3-6-ubuntu-linuxmint/

- **Install Python 3.6 in virtualenv**:
    1. https://snakeycode.wordpress.com/2017/11/18/working-in-python-3-6-in-ubuntu-14-04/
       (python3.6 -m venv full-path-to-venv-dir)

- **Install Mysql 5.7**
    https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-14-04

- **Running Test**:
    gitlab CI doc: https://docs.gitlab.com/runner/
    Tutorial:
        https://docs.python.org/3/library/unittest.html#command-line-options
        https://www.youtube.com/watch?v=Hs8LCilGVaM (start at 25th min)
    to run and test locally: python -m unittest discover

## Usage
    client_secret: Simpl specified client-secret key
    is_prod: to hit sandbox/production environment urls of Simpl

    Initialize client:
    client = Client(client_secret=client_secret, is_prod=True/False)

    To check for valid-customer:
    client.approval.check_simpl_approval(payload=payload)

    To charge customer:
    client.payment.charge_token(payload=payload)

    Note: for payloads, refer:https://sandbox.getsimpl.com/docs/web/custom