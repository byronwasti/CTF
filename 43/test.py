from PIL import Image as img
import lendianSteganography as steg

test = img.open("img.bmp")

items = list(test.getdata(2))

print ''.join([chr(i) for i in items])


bits = []
for i in items:
    lendian = i & 1
    bits.append(lendian)

for i in xrange(8):
    char = 0
    for j in bits[i:i+8]:
        char = char << 1
        if j == 0:
            char = char & ~1
        else:
            char = char | 1

    #print chr(char)
#print steg.decode(items)
