import sys
import time

for i in range(0,51):
    
    sys.stdout.write("{} [{} {}]\r".format(i, '#'*i, "."*(50-i)))
    sys.stdout.flush()
sys.stdout.write("\n")

print(sys.argv)

if len(sys.argv) != 4:
    print("[X] To run {} you must enter a username and password".format(sys.argv[0]))

First_name = sys.argv[1]
Last_name = sys.argv [2]
Password = sys.argv[3]

print("{} {} {}".format(First_name, Last_name, Password))
