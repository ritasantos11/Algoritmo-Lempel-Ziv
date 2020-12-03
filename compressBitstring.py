from bitstring import BitArray, BitStream
import math, sys


data = open(sys.argv[1], "rb")
print(data)
bitstring = BitArray(data)
print(bitstring)
print(bitstring.bin)


x = BitArray()
output = BitArray('0b0')     # bitstring
c = BitArray('0b0')

#output = bitstring.bin[0]       # string
#for bit in bitstring.cut(1):
#    output += bit
#    c += bit
#    break
#print(output)
#print(type(c))

#c = bitstring.bin[0]


list = [""]
index = 0
sec_index = 0
i = 0

newloop = False
y_list = False

while index < len(bitstring):
    #print(type(c))
    if newloop == False:
        #x = bitstring.bin[index]
        x = bitstring[index:index+1]
        sec_index = 0
    else:
        #x += bitstring.bin[index]
        x = bitstring[index-sec_index:index+1]
        newloop = False
    
    print("\nXXXXXX:" + str(x))
    print("index:" + str(index))
    for elem in list:
        if elem == x:
            newloop = True
            sec_index += 1
            break
    
    if newloop == False:
        if len(str(x)) == 1:
            y = ""
            b = x
        else:
            y = x[0:len(x)-1]
            print("Y:" + str(y))
            b = x[-1:]
            print("B:" + str(b))
        
        for elem in list:
            if elem == y:
                y_list = True
                i = list.index(elem)
                break

        if y_list == True:
            binary_i = "{0:b}".format(i)
            
            if len(binary_i) < math.log(len(list),2):
                count = 0
                while count < math.log(len(list),2)-1:
                    c.append('0b0')
                    count += 1
            
            print("binary:" + str(binary_i))
            c.append(bin(i))
            #print("c:" + str(c))
            c.append(b)
            c = c[1:len(c)]
            #print(type(c))
            print("c:" + str(c))
            
        output.append(c)

        list.append(x)

    index += 1
    y_list = False
    c = BitArray('0b0')
    

# sobra bits


output = output[1:len(output)]
print(output.bin)

"""
output_bytes = ""
for byte in output.cut(8):
    print(byte)
    output_bytes += byte

print(output_bytes)


data.close()

output_file = open(sys.argv[2], "wb")
output_file.write(output_bytes.hex)
"""

