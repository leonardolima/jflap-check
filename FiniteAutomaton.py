import parser
import ast
import sys
import getopt
import os
from subprocess import call
from Exceptions import DefinitionError
from Templates import HTMLTemplate

class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial, final):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.initial = initial
        self.final = set(final)
        self.current_state = initial
        self.validate()

    def __repr__(self):
        return ''

    def __len__(self):
        return len(self.states)

    def run(self, str):
        for c in str:
            for char, state in self.transitions[self.current_state]:
                if (c == char):
                    self.current_state = state
        return self.current_state

    def is_accepted(self):
        return self.current_state in self.final

    def simulate(self, str):
        '''
        Simulates the input without changing the state.
        '''
        temp_state = self.current_state
        for c in str:
            for char, state in self.transitions[temp_state]:
                if (c == char):
                    temp_state = state
        return temp_state
    def fromregexp(re):
        '''
        Generates a automaton that is equivalent to the given regular expression.
        '''

    def copy(self):
        return FiniteAutomaton(self.states, self.alphabet, self.transitions, self.initial, self.final)

    def reset(self):
        self.current_state = self.initial

    def regexp(self):
        '''
        Generates a regular expression that recognizes the same language.
        '''

    def validate(self):
        '''
        Checks if the initial and final states are valid, and if every state has all transitions.
        '''
        if not len(self.states) > 0:
            raise DefinitionError('There must be at least one state.')
        if not len(self.alphabet) > 0:
            raise DefinitionError('Alphabet cannot be empty.')
        if self.initial not in self.states:
            raise DefinitionError('Initial state most by part of the automaton states.')
        if not self.final <= self.states:
            raise DefinitionError('Final states must by part of the automaton states.')

    def check(self, str):
        self.run(str)
        if self.current_state in self.final:
            return True
        else:
            return False

    def toHTML(self, name='FiniteAutomaton'):
        '''
        Generates an HTML file with a graph representing the automaton.
        '''
        html = HTMLTemplate.render(self)
        f = open(name + '.html', 'w')
        f.write(html)
        f.close()

def convert(ast):

    def getStatesAndTransitions(node):
        if node:
            if node.type != 'automaton':
                l = list()
                for c in node.children:
                    l += getStatesAndTransitions(c)
                return l
            else:
                states = list()
                transitions = list()
                for c in node.children:
                    if c.type == 'state':
                        states.append(c)
                    elif c.type == 'transition':
                        transitions.append(c)
                return states, transitions
        else:
            return []

    states, transitions = getStatesAndTransitions(ast)

    _states = list()
    _alphabet = list()
    _final = list()
    _transitions = {}
    dictionary = {}
    initial = ''

    for state in states:
        i, n = None, None

        for c in state.children:
            if c.type == 'statename':
                n = c.value
                _states.append(c.value)
            if c.type == 'id':
                i = c.value
            if c.type == 'initial':
                initial = n
            if c.type == 'final':
                _final.append(n)
        dictionary[i] = n

    for transition in transitions:
        _from, _to, sym = None, None, None

        for c in transition.children:
            if c.type == 'from':
                _from = dictionary[c.value]
            elif c.type == 'to':
                _to = dictionary[c.value]
            elif c.type == 'read':
                sym = c.value
                _alphabet.append(sym)
            if _from and _to and sym and _from in _transitions:
                _transitions[_from] = [(sym, _to)] + _transitions[_from]
            elif _from and _to and sym:
                _transitions[_from] = [(sym, _to)]

    __states = set(_states)
    alphabet = set(_alphabet)
    final = set(_final)

    a = FiniteAutomaton(__states, alphabet, _transitions, initial, final)
    return a

def usage():
    print "Usage: "
    print " python FiniteAutomaton.py --input <file>.jff"

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:", ["input="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    f = None

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exist(2)
        elif opt in ("-i", "--input"):
            try:
                f = open(arg, 'r')
            except (OSError, IOError) as e:
                usage()
                sys.exit(2)
            p = parser.Parser()
            ast = p.parse(f.read())
            if ast == None:
                print "ERROR! The file " + arg + " is not valid"
            else:
                print "AST was successfully built. Generating Finite Automata..."
                a = convert(ast)
                a.toHTML()
                print "FiniteAutomata.html was successfully generated! :)"

if __name__ == '__main__':
    main()
