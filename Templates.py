from jinja2 import Environment, FileSystemLoader
import os

env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'data', 'templates')),
    block_start_string='[%',
    block_end_string='%]',
    variable_start_string='[[',
    variable_end_string=']]',
)

class HTMLTemplate(object):

    @staticmethod
    def render(automaton):
        t = env.get_template('FiniteAutomaton.html')
        return t.render(title='test', states=automaton.states, transitions=automaton.transitions
        , initial=automaton.initial, final=automaton.final)
