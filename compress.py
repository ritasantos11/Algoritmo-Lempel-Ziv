from bitstring import BitArray
import math, sys


data = open(sys.argv[1], "rb")
bitstring = BitArray(data)
data.close()
#print(bitstring.bin)


x = BitArray()
c = BitArray()
output = BitArray()


list = {"": 0}

list_index = 1
index = 0
sec_index = 0
i = 0

newloop = False
y_list = False

while index < len(bitstring):
    if newloop == False:
        x = bitstring[index:index+1]
        sec_index = 0
    else:
        x = bitstring[index-sec_index:index+1]
        newloop = False

    if x.bin in list:
        newloop = True
        sec_index += 1

    if newloop == False:
        if len(x) == 1:
            y = ""
            b = x
        else:
            y = x[0:len(x)-1]
            b = x[-1:]
        
        if len(x) != 1:
            if y.bin in list:
                y_list = True
                i = list.get(y.bin)
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
            
            if len(list) != 1:
                c.append(bin(i))
            c.append(b)
            
        output.append(c)

        list[x.bin] = list_index
        list_index += 1

    index += 1
    y_list = False
    c = BitArray()
    


### sobra bits
if len(x) != 0:
    index = 0
    r = BitArray()

    while index < len(x):
        if x.bin[index:index+1] == '0':
            r.append('0b000')
        else:
            r.append('0b111')
        index += 1

    output.append(r)

    # nº de bits que sobrou do algoritmo
    num_bits_extra_binary = bin(len(x))

    # nº bits que sobrou do algoritmo em 8 bits
    num_bits_extra_binary_8 = BitArray()
    count = len(num_bits_extra_binary) - 2
    while count%8 != 0:
        num_bits_extra_binary_8.append('0b0')
        count += 1

    num_bits_extra_binary_8.append(num_bits_extra_binary)
    output.append(num_bits_extra_binary_8)

    # nº bytes que o nº bits que sobrou do algoritmo ocupa
    num_bytes_binary_8 = BitArray()
    num_bytes = int(count/8)
    num_bytes_binary = bin(num_bytes)
    count = len(num_bytes_binary) - 2
    while count < 8:
        num_bytes_binary_8.append('0b0')
        count += 1

    num_bytes_binary_8.append(num_bytes_binary)
    output.append(num_bytes_binary_8)

else:
    output.append('0b00000000')


### acrescentar 0s p ser multiplo de 8
num_bits = len(output.bin) % 8
if num_bits != 0: 
    index = num_bits
    while index < 8:
        output.append('0b0')
        index += 1

    # nº bits que antes tinham sobrado e que por isso se acrescentou 0s para fzr 1 byte
    num_bits_binary = bin(num_bits)
    size = len(num_bits_binary) - 2
    while size != 8:
        output.append('0b0')
        size += 1

    output.append(num_bits_binary)

else:
    output.append('0b00000000')


#print(output.bin)


output_bytes = []
for byte in output.cut(8):
    output_bytes.append(byte.uint)


output_file = open(sys.argv[2], "wb")
output_file.write(bytearray(output_bytes))
output_file.close()


