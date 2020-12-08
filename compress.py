from bitstring import BitArray, BitStream
import math, sys


data = open(sys.argv[1], "rb")
print(data)
bitstring = BitArray(data)
print(bitstring)
print(bitstring.bin)
data.close()


x = BitArray()
output = BitArray()     # bitstring
c = BitArray()

#output = bitstring.bin[0]       # string
#c = bitstring.bin[0]


#list = [""]
list = {"": 0}

list_index = 1
index = 0
sec_index = 0
i = 0

newloop = False
y_list = False

while index < len(bitstring):
    if newloop == False:
        #x = bitstring.bin[index]
        x = bitstring[index:index+1]
        sec_index = 0
    else:
        #x += bitstring.bin[index]
        x = bitstring[index-sec_index:index+1]
        newloop = False
    
    #print("\nXXXXXX:" + str(x.bin))
    #print("index:" + str(index))
    """
    for elem in list:
        if elem == x:
            newloop = True
            sec_index += 1
            break
    """

    if x.bin in list:
        newloop = True
        sec_index += 1

    if newloop == False:
        if len(x) == 1:
            y = ""
            #print("Y:" + str(y))
            b = x
            #print("B:" + str(b))
        else:
            y = x[0:len(x)-1]
            #print("Y:" + str(y))
            b = x[-1:]
            #print("B:" + str(b))
        
        """
        for elem in list:
            if elem == y:
                y_list = True
                i = list.index(elem)
                break
        """
        
        if len(x) != 1:
            if y.bin in list:
                y_list = True
                i = list.get(y.bin)
                #print("I:" + str(i))
        else:
            y_list = True
            i = 0

        if y_list == True:
            binary_i = bin(i)
            
            if len(binary_i)-2 < math.ceil(math.log(len(list),2)):
                count = len(binary_i)-2
                while count < math.ceil(math.log(len(list),2)):
                    c.append('0b0')
                    count += 1
            
            #print("binary:" + str(binary_i))
            if len(list) != 1:
                c.append(bin(i))
            c.append(b)
            #c = c[1:len(c)]
            #print(type(c))
            #print("c:" + str(c.bin))
            
        output.append(c)
        #print("OUTPU:" + str(output.bin))

        #list.append(x)
        list[x.bin] = list_index
        list_index += 1
        #print("SIZE LIST:" + str(len(list)))

    index += 1
    #list_index += 1
    y_list = False
    c = BitArray()
    

# sobra bits
print("XXX:" + str(x.bin))
index = 0
d = BitArray()

while index < len(x):
    if x.bin[index:index+1] == '0':
        d.append('0b000')
    else:
        d.append('0b111')
    index += 1

#print(d)
output.append(d)
#output = output[1:len(output)]
print(output.bin)


output_bytes = []
#print(len(output))
for byte in output.cut(8):
    #print(byte.bin)
    #print(type(byte))
    output_bytes.append(byte.hex)

#print(output_bytes)
#print(type(output_bytes))


print(len(output))
with open(sys.argv[2], "wb") as output_file:
    output_file.write(bytearray(int(i,16) for i in output_bytes))

#output_file.write(output_bytes)


