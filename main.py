import parser, ast, sys

def prt(element, level=1):
    '''Exibe os elementos no terminal'''
    if element is not None:
        print(' '*level + str(element))
        for e in element.children:
            prt(e, level + 2)

def main():
    f = open(sys.argv[1], 'r')
    p = parser.Parser()
    result = p.parse(f.read())
    prt(result)

if __name__ == '__main__':
    main()
