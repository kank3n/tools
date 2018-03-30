import sys, struct

def single_byte_xor():
    input = open(sys.argv[1], "rb").read()
    output = open(sys.argv[1]+".encrypted", "w")
    key = int(sys.argv[2])

    data = ""
    for d in input:
        data +=  struct.pack("B", int(struct.unpack("B", d)[0]) ^ key)

    output.write(data)
    output.close()
    print sys.argv[1]+".encrypted"+" has been created!"

if __name__ == "__main__":
    single_byte_xor()
