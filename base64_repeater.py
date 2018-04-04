import sys, base64

def encode(text, times):
    for i in range(int(times)):
        text = base64.b64encode(text)
    print text

def decode(file, word):
    i = 0
    text = open(file).read()
    while True:
        text = base64.b64decode(text)
        i += 1
        if word in text:
            print ""
            print "Word[\"" + word + "\"] was found."
            print str(i) + " times tried."
            print ""
            print "Decoded Text: " + text
            break

def usage():
    print '''
    To encode text:
    python base64_repeater.py -e <text> <times>

    To decode text:
    python base64_repeater.py -d <file> <search word>
    '''

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '-e':
        encode(sys.argv[2], sys.argv[3]) 
    elif len(sys.argv) > 1 and sys.argv[1] == '-d':
        decode(sys.argv[2], sys.argv[3])
    else:
        usage()
