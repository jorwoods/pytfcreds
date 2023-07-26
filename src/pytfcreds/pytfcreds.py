"""Main module."""
import getpass
import json
import sys

import keyring

from pytfcreds.exceptions import MissingCredentials


def get(host: str, user: str) -> int:
    try:
        print(json.dumps({"token": keyring.get_credential(host, user).password}))
    except:
        print(f"No credentials found for {user}@{host}", file=sys.stderr)
        return 1
    else:
        return 0


def store(host: str, user: str) -> int:
    try:
        keyring.set_password(host, user, getpass.getpass())
    except:
        print(f"Error setting password for {user}@{host}", file=sys.stderr)
        return 1
    else:
        return 0


def forget(host: str, user: str) -> int:
    try:
        keyring.delete_password(host, user)
    except:
        print(f"Error forgetting password for {user}@{host}")
        return 1
    else:
        return 0
