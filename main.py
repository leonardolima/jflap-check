import lexer, sys

def main():
	f = open(sys.argv[1], 'r')
	l = lexer.Lexer()
	l.test(f.read())

if __name__ == '__main__':
	main()
