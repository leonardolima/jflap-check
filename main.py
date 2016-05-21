import parser, sys

def main():
    f = open(sys.argv[1], 'r')
    p = parser.Parser()
    p.parse(f.read())

if __name__ == '__main__':
    main()
