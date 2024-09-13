import sys

def cat(filename):
    f = open(filename, 'r')
    # for line in f:
    #     print(line,end='')
    # lines = f.readlines()
    # print(lines)
    text = f.read()
    print(text)
    f.close()

def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()
