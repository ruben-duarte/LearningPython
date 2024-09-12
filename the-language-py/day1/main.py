import sys

def Hello(name):
    if name == 'george'or name == 'nick':
        print('Alert: George Mode')  
        name += '!???'
    else:
        DoesNotexist(name)
        print('else nick')
    name = name + '!!!'
    print('Hello', name)

def main():
    Hello(sys.argv[1])

if __name__ == '__main__':
    main()

