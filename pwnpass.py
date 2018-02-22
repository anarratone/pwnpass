"""
Query Pwned Passwords.

Small utility to query Troy Hunt's Pwned Passwords V2 database while preserving
privacy by means of the range feature of pwnedpasswords API.
"""

import sys

import hashlib
import getpass
import requests


def main():
    """Query the database in a privacy protection manner."""
    password_hash = hashlib.sha1(
        getpass.getpass(
            "Insert the password to look for (no input is shown): ")).hexdigest().upper()
    if password_hash != hashlib.sha1(
            getpass.getpass("Retype your password: ")).hexdigest().upper():
        print "ERROR: Passwords do not match!"
        return
    response = requests.get("https://api.pwnedpasswords.com/range/{}".format(password_hash[:5]))
    if response.status_code == 200:
        for line in response.text.split("\r\n"):
            if password_hash[5:] in line:
                _, occurrences = line.split(":")
                print "WARNING: Your password has been seen {} times in the database! ".format(
                    occurrences)
                print "Please change your password immediately!"
                return
        print "CONGRATULATIONS! You are not in the leaked passwords database!"


if __name__ == "__main__":
    sys.exit(main())
