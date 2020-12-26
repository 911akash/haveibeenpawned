
import sys
import hashlib
import argparse
import urllib.request
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('password', help='give password as positional parameter in string without quotes')
args = parser.parse_args()


input_str = args.password
# get SHA1 hash
sha_1 = hashlib.sha1(input_str.encode('utf-8'))
sha_hex = sha_1.hexdigest()
print('checking.......')

# GET the target URL
first5 = sha_hex[0:5].upper()
target_url = "https://api.pwnedpasswords.com/range/{}".format(first5)
ret = urllib.request.urlopen(target_url)

# write in memory and check if match
with tempfile.TemporaryFile(mode='w+b') as temp_file:
    temp_file.write(ret.read())
    temp_file.seek(0)
    arr = temp_file.read().decode('utf-8').split()
    found = False
    number = ''
    for item in arr:
        if sha_hex[5:].upper() == item.strip().split(':')[0].upper():
            found = True
            number = item.strip().split(':')[1]
            break
    if found:
        print("This password has been breached : {} times. So CHANGE IT !! ".format(number))
    else:
        print("cool! your password is safe so far !! No need to worry i havent posted it anywhere online.")

print("target url : {}".format(target_url))
print("SHA-1 hash to be looked for: {}".format(sha_hex[5:].upper()))