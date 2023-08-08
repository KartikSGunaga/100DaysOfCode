import string

process = input("Type 'enc' to encode and 'dec' to decode: ")

message = input("Type your message: ")

shift = int(input('Type the shift number: '))

if(shift > 26):
    print("Invalid shift")
    exit()

l_msg = []
encrypt_msg = []

for i in range(len(message)):
    l_msg.append(message[i])

# print("the message entered is: ", str(l_msg))
alphabets = string.ascii_lowercase
length = len(alphabets)
# print(f"The length of alpha: {length} and length-1 : {length-1}")
# print(alphabets.index("z"))

def encode(l_msg):
    for j in l_msg:
        print(f"The current character is {j}")
        if(j in string.punctuation or j in string.whitespace or j.isdigit()):
            encrypt_msg.append(j)
            continue
        else:
            pos = alphabets.index(j)
            # print(pos)

            if(pos + shift > length -1):
                index = abs(26 - pos - shift)
                print(f"The index of {j} is: {pos} and shifted index is : {index}")
            else:
                index = pos + shift
                print(f"The index of {j} is: {pos} and shifted index is : {index}")

            encrypt_msg.append(alphabets[index])

    final_msg = "".join(encrypt_msg)
    return final_msg
        
def decode(l_msg):
    for j in l_msg:
        print(f"The current character is {j}")
        if(j in string.punctuation or j in string.whitespace or j.isdigit()):
            encrypt_msg.append(j)
            continue
        else:
            pos = alphabets.index(j)

            if(pos - shift < 0):
                index = 26 - shift + pos
                #print(f"The index of {j} is: {pos} and shifted index is : {index}")
            else:
                index = pos - shift
                #print(f"The index of {j} is: {pos} and shifted index is : {index}")

            encrypt_msg.append(alphabets[index])

    final_msg = "".join(encrypt_msg)
    return final_msg

if(process == 'enc'):
    print(f"The encrypted message is: {encode(l_msg)}")
elif(process == 'dec'):
    print(f"The decrypted message is: {decode(l_msg)}")
else:
    print("Invalid process inputted.")
            

        