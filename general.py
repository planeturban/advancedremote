from time import sleep

def mkcmd(lingo, s):
    s = s.decode("hex")
    sum = 0;
    s = chr(len(s) + 1) + chr(lingo) + s
    for ch in s:
        sum = sum + ord(ch)
    sum = 0x100 - (sum & 0xff)
    return chr(0xff) + chr(0x55) + s + chr(sum)

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    return reduce(lambda x,y:x+y, lst)

def inttohexstr(x, length = 4):
    if ( x > 4294967295 ): # Boy, do you have a large library!
        x = 4294967295 # Probably redundant..
    length = length * 2
    return hex(x).split("x")[1].zfill(length)


def printhex(s):
    return ":".join("{:02x}".format(ord(c)) for c in s)

def readResponse( serial, fullMessage = False):
    ret = ()
    sleep(.15) # need to wait a while, just in case..
    while serial.inWaiting():
        if serial.read(2) == "ff55".decode("hex"):
            length = serial.read(1)
            lingo = serial.read()
            body = serial.read(int(toHex(length), 16)-1)
            checksum = serial.read()
            message = "ff55".decode("hex") + length + lingo + body + checksum
            if mkcmd(int(toHex(lingo)), toHex(body)) == message:
                if not fullMessage:
                    ret = ret + (body,)
                else:
                    ret = ret +  (message, )
    return ret
