#!/usr/bin/env python
import sys, os, time, random
import binascii
file=sys.argv[1]

if len(sys.argv) > 2:
    rate=float(sys.argv[2])
else:
    rate=0.01

try:
    ret = raw_input("This will irreversibly corrupt the file {} by {}%. Are you sure? (type 'yes')".format(file,rate*100))
except:
    ret = input("This will irreversibly corrupt the file {} by {}%. Are you sure? (type 'yes')".format(file,rate*100))
if ret != 'yes':
    print('Okay, not corrupting.')
    exit(10)

size = os.stat(file).st_size
amount = int(size*rate)

print('File size is {}, corrupting {} bytes:'.format(size, amount))
time.sleep(1)

random.seed()
with open(file,'rb+') as f:
    for x in range(amount):
        if (x % max(1,int(amount/100))) == 0:
            print('{}%'.format(round(float(x)/amount*100,2)))
        seek = random.randrange(size)
        if sys.version_info[0] < 3:
            byte = chr(random.randint(0,255))
        else:
            byte = bytes([random.randint(0,255)])
        f.seek(seek)
        readbyte = f.read(1)
        print('Seeking to {}, converting {} to {}'.format(seek,binascii.hexlify(readbyte).decode(),
                                                                  binascii.hexlify(byte).decode()))
        f.seek(seek)
        f.write(byte)
print('Done!')
