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

        for state in self.states:
            state_transitions = dict(self.transitions[state])
            for letter in self.alphabet:
                if letter not in state_transitions:
                    raise DefinitionError('Invalid transition function.')

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

def main():
    states = {'q1', 'q2', 'q3', 'q4', 'q5'}
    alphabet = {'a', 'b'}
    initial = 'q1'
    final = {'q4'}
    delta = {'q1': [('a', 'q5'), ('b', 'q2')],
             'q2': [('a', 'q2'), ('b', 'q3')],
             'q3': [('a', 'q5'), ('b', 'q4')],
             'q4': [('a', 'q5'), ('b', 'q5')],
             'q5': [('a', 'q5'), ('b', 'q5')]}
    a = FiniteAutomaton(states, alphabet, delta, initial, final)
    a.toHTML()

if __name__ == '__main__':
    main()
