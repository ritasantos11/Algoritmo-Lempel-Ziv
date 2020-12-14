from bitstring import BitArray
import math, sys

data = open(sys.argv[1], "rb")
print(data)
complete_bitstring = BitArray(data)
#complete_bitstring.append('0b01')
print(complete_bitstring)
print(complete_bitstring.bin)

num_extra_bits = complete_bitstring[-8:]
print(num_extra_bits)
num = int(num_extra_bits.bin, 2)
print(num)

bitstring = complete_bitstring[0:len(complete_bitstring)-(num+8)]
print(bitstring.bin)

r_bitstring = complete_bitstring[len(complete_bitstring)-(num+8):len(complete_bitstring)-8]
print(r_bitstring.bin)

x = BitArray()
output = BitArray()
i = BitArray()
y = BitArray()

list = {0 : ""}

list_index = 1
read_index = 0
index = 0

y_list = False

while index < len(bitstring):
        #print("INDEX:" + str(index))
        if len(list) == 1:
            x.append(bitstring[0:1])
            index += 1

        else:
            while read_index < math.ceil(math.log(len(list),2)):
                #print("ola")
                i.append(bitstring[index:index+1])
                read_index += 1
                index += 1
            
            b = bitstring[index:index+1]
            index += 1
            int_i = i.uint
            #print(list)
            #print(type(int_i))
            if int_i in list:
                #print(int_i)
                #print(type(y))
                a = list.get(int_i)
                #print(a)
                #print(type(a))
                y.append(a)
                y_list = True

            
            if y_list == True:
                #print(y)
                x.append(y)

            x.append(b)

        list[list_index] = x
        output.append(x)
        
        list_index += 1
        #index += 1
        read_index = 0

        i = BitArray()
        x = BitArray()
        y = BitArray()

        y_list = False


index = 0
while index < len(r_bitstring.bin):
    if r_bitstring.bin[index:index+1] == '0':
        output.append('0b0')
        index += 3
    else:
        output.append('0b1')
        index += 3


print(output)
print(output.bin)
print(len(output.bin)%8)

output_bytes = []
#print(len(output))
for byte in output.cut(8):
    #print(byte.bin)
    #print(type(byte))
    output_bytes.append(byte.hex)

output_file = open(sys.argv[2], "wb")
output_file.write(bytearray(int(i,16) for i in output_bytes))

