import parser
import ast
import sys
import getopt
import os
from subprocess import call

def usage():
    print "Usage: "
    print " python check.py --input filename.jff --print (optional)"
    print " python check.py --clean"

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:pc", ["input=", "print", "clean"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    f = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exist(2)
        if opt in ("-i", "--input"):
            try:
                f = open(arg, 'r')
            except (OSError, IOError) as e:
                usage()
                sys.exit(2)                
            p = parser.Parser()
            result = p.parse(f.read())
            if result == None:
                print "ERROR! The file " + arg + " is not valid"
            else:
                print "Parse table successfully generated!"
        elif opt in ("-p", "--print"):
            if result == None:
                print "Can not print AST because it's empty"
            else:
                print result
        elif opt in ("-c", "--clean"):
            try:
                call(["pyclean", "."])
                os.remove("parser.out")
                os.remove("parsetab.py")
            except OSError as e:
                print e

if __name__ == '__main__':
    main()
