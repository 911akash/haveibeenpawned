
import sys
import hashlib
import argparse
import urllib.request
import tempfile


def _req(target_url):
    return urllib.request.urlopen(target_url)

def target_url(sha_hex):
    first5 = sha_hex[0:5].upper()
    target_url = "https://api.pwnedpasswords.com/range/{}".format(first5)
    return _req(target_url) , target_url

def get_sha_digest(password):
    sha_1 = hashlib.sha1(password.encode('utf-8'))
    return sha_1.hexdigest() 

def match_no_match(ret, sha_hex):
    # write in memory and check if match
    with tempfile.TemporaryFile(mode='w+b') as temp_file:
        # temp_file.write(ret.read())
        temp_file.write(ret)
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
            return True, number
        else:
            return False, 0

def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('password', help='give password as positional parameter in string without quotes')
    return parser 

def main(args):
    args = get_argument_parser().parse_args(args)
    input_str = args.password
    # get SHA1 hash
    sha_hex = get_sha_digest(input_str)
    print('checking.......')

    # GET the target URL
    ret , targeturl = target_url(sha_hex)

    ret = ret.read()
    #match , no-match
    print(type(ret))
    found, num = match_no_match(ret, sha_hex)
    print("************************************************************************")
    if found:
        print("This password has been breached : {} times. So CHANGE IT !! ".format(num))
    else:
        print("cool! your password is safe so far !! No need to worry i havent posted it anywhere online.")
    print("************************************************************************")
    print("target url : {}".format(targeturl))
    print("SHA-1 hash to be looked for: {}".format(sha_hex[5:].upper()))