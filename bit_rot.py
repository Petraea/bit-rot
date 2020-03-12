#!/usr/bin/env python
import sys, os, time, random
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
amount = int(size*rate*8)

print('File size is {} bits, corrupting {} bits:'.format(size*8, amount))
time.sleep(1)

random.seed()
with open(file,'rb+') as f:
    for x in range(amount):
        if (x % max(1,int(amount/100))) == 0:
            print('{}%'.format(round(float(x)/amount*100,2)))
        seek = random.randrange(size)

        f.seek(seek)
        readbyte = ord(f.read(1))
        bit = 2**random.randint(0,7)
        if readbyte & bit:
            byte = readbyte - bit
        else:
            byte = readbyte + bit

        print('Seek: {}, change {:02x} to {:02x}'.format(seek,readbyte,byte))
        f.seek(seek)
        if sys.version_info[0] < 3:
            f.write(chr(byte))
        else:
            f.write(bytes([byte]))
print('Done!')
