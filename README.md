# pwnpass
Python script to query Troy Hunt's Pwned Passwords database.

The script queries the database using the _range_ feature, i.e. it never
discloses the cleartext password or its full hash. Only the first 5 digits
of the hash are transmitted over HTTPS, the rest is computed locally.

To use install the requirements:
```
pip install -f requirements.txt
```
and the run the script:
```
python pwnpass.py
```
