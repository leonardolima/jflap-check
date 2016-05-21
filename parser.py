import lexer, ply.lex as lex, ply.yacc as yacc
from ast import Element
from lexer import tokens

class Parser(object):

    def __init__(self):
        self.tokens = tokens
        self.lexer = lex.lex(module=lexer)
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        return self.parser.parse(data)

    def p_structure(self, p):
        '''structure    : LSTRUCTURE type tapes body RSTRUCTURE'''

        p[0] = Element(type='structure', children=[p[2], p[3], p[4]])

    def p_type(self, p):
        '''type         : LTYPE VALUE RTYPE'''

        p[0] = Element(type='type', value=p[2])

    def p_tapes(self, p):
        '''tapes        : LTAPES VALUE RTAPES
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='tapes', value=p[2])

    def p_body(self, p):
        '''body         : expression
                        | automaton
                        | productions'''

        p[0] = p[1]

    # Regular Expression
    def p_expression(self, p):
        '''expression   : LEXPRESSION VALUE REXPRESSION'''

        p[0] = Element(type='expression', value=p[2])

    #Finite Automata, Push-dowm Automata, Turing Machine
    def p_automaton(self, p):
        '''automaton    : LAUTOMATON blocks states transitions RAUTOMATON'''

        p[0] = Element(type='automaton', children=[p[2], p[3], p[4]])

    def p_blocks(self, p):
        '''blocks       : block blocks
                        | empty'''

        self.make_list(p)

    def p_block(self, p):
        '''block        : LBLOCK tag x y RBLOCK'''

        p[0] = Element(type='block', children=[p[2], p[3], p[4]])

    def p_tag(self, p):
        '''tag          : LTAG VALUE RTAG'''

        p[0] = Element(type='tag', value=p[2])

    def p_states(self, p):
        '''states       : state states
                        | empty'''

        self.make_list(p)

    def p_state(self, p):
        '''state        : LSTATE x y special output RSTATE'''

        p[0] = Element(type='state', children=[p[2], p[3], p[4], p[5]])

    def p_x(self, p):
        '''x            : LX VALUE RX'''

        p[0] = Element(type='x', value=p[2])

    def p_y(self, p):
        '''y            : LY VALUE RY'''

        p[0] = Element(type='y', value=p[2])

    def p_special(self, p):
        '''special      : initial final'''

        p[0] = [p[1], p[2]]

    def p_initial(self, p):
        '''initial      : INITIAL
                        | empty'''

        p[0] = None if p[1] is None else Element(type='initial')

    def p_final(self, p):
        '''final        : FINAL
                        | empty'''

        p[0] = None if p[1] is None else Element(type='final')

    def p_output(self, p):
        '''output       : LOUTPUT VALUE ROUTPUT
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='output', value=p[2])

    def p_transitions(self, p):
        '''transitions  : transition transitions
                        | empty'''

        self.make_list(p)

    def p_transition(self, p):
        '''transition   : LTRANSITION from to read pop push transout write move RTRANSITION'''

        p[0] = Element(type='transition', children=[p[2], p[3], p[4], p[5], p[6], p[7]])


    def p_from(self, p):
        '''from         : LFROM VALUE RFROM'''

        p[0] = Element(type='from', value=p[2])

    def p_to(self, p):
        '''to           : LTO VALUE RTO '''

        p[0] = Element(type='to', value=p[2])

    def p_read(self, p):
        '''read         : READ
                        | LREAD VALUE RREAD
                        | LREAD empty RREAD'''

        p[0] = Element(type='read') if len(p) < 3 else Element(type='read', value=p[2])

    def p_pop(self, p):
        '''pop          : LPOP VALUE RPOP
                        | POP empty
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='pop', value=p[2])

    def p_push(self, p):
        '''push         : LPUSH VALUE RPUSH
                        | PUSH empty
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='push', value=p[2])

    def p_transout(self, p):
        '''transout     : LTRANSOUT VALUE RTRANSOUT
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='transout', value=p[2])

    def p_write(self, p):
        '''write        : LWRITE VALUE RWRITE
                        | WRITE empty
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='write', value=p[2])

    def p_move(self, p):
        '''move         : LMOVE VALUE RMOVE
                        | empty'''

        p[0] = None if len(p) < 3 else Element(type='move', value=p[2])

    # Context-free Grammar

    def p_productions(self, p):
        '''productions  : production productions
                        | empty'''
        self.make_list(p)


    def p_production(self, p):
        '''production   : LPRODUCTION left right RPRODUCTION'''

        p[0] = Element(type='production', children=[p[2], p[3]])

    def p_left(self, p):
        '''left         : LLEFT VALUE RLEFT'''

        p[0] = Element(type='left', value=p[2])

    def p_right(self, p):
        '''right        : LRIGHT VALUE RRIGHT
                        | LRIGHT empty RRIGHT
                        | RIGHT empty'''

        p[0] = Element(type='right', value=p[2])

    #empty transition
    def p_empty(self, p):
        '''empty        :'''

        p[0] = None

    def make_list(self, p):
        if p[0] is None:
            p[0] = []
        if p[1] is not None:
            p[0].append(p[1])
        if len(p) == 3 and p[2] is not None:
            p[0] = p[0] + p[2]

    # Error rule for syntax errors
    def p_error(self, p):
        if p:
            print("Syntax error at token", p.type)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        # else:
            # print("Syntax error at EOF")
