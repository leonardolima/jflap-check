# JFLAP-Check

A simple verifier written in Python to check if the syntax of a JFLAP file (.jff) is correct. We are using [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/) to specify the grammar and build the Abstract Syntax Tree.

#### Usage:

* To check if the syntax of *<file>* is correct or not:
  ```
  $ python check.py -i (or --input) <file>.jff -p (or --print, this command is optional)
  ```

* To clean the directory:
  ```
  $ python check.py -c (or --clean)
  ```