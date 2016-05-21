import lexer as l, ply.lex as lex, ply.yacc as yacc

class Parser(object):

    def __init__(self):
        self.tokens = l.tokens
        self.lexer = lex.lex(module=l)
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        self.parser.parse(data)
        # self.lexer.input(data)
        #
        # # Tokenize
        # while True:
        #     tok = self.lexer.token()
        #     if not tok:
        #         break      # No more input
        #     print(tok)

    def p_structure(self, p):
        'structure : LSTRUCTURE LTYPE VALUE RTYPE body RSTRUCTURE'
        pass

    def p_body(self, p):
        'body : LAUTOMATON automaton RAUTOMATON'
        pass

    def p_automaton(self, p):
        '''automaton : states transitions'''
        pass

    def p_states(self, p):
        '''states : state states
                | empty'''
        pass

    def p_state(self, p):
        'state : LSTATE LX VALUE RX LY VALUE RY special output RSTATE'
        pass

    def p_special(self, p):
        '''special : INITIAL
                    | FINAL
                    | empty'''
        pass

    def p_state_output(self, p):
        '''output : LOUTPUT VALUE ROUTPUT
                    | empty'''

    def p_transitions(self, p):
        '''transitions : transition transitions
                    | empty'''
        pass

    def p_transition(self, p):
        'transition : LTRANSITION LFROM VALUE RFROM LTO VALUE RTO read pop push transout write move RTRANSITION'
        pass

    def p_transition_read(self, p):
        '''read : READ
                | LREAD VALUE RREAD
                | LREAD empty RREAD'''
        pass

    def p_transition_pop(self, p):
        '''pop : POP
                | LPOP VALUE RPOP
                | empty'''
        pass

    def p_transition_push(self, p):
        '''push : PUSH
                 | LPUSH VALUE RPUSH
                 | empty'''
        pass

    def p_transition_transout(self, p):
        '''transout : LTRANSOUT VALUE RTRANSOUT
                    | empty'''
        pass

    def p_transition_write(self, p):
        '''write : LWRITE VALUE RWRITE
                    | WRITE
                    | empty'''

    def p_transition_move(self, p):
        '''move : LMOVE VALUE RMOVE
                | empty'''

    def p_productions(self, p):
        '''productions : production productions
                    | empty'''
        pass

    def p_production(self, p):
        'production : LPRODUCTION LLEFT VALUE RLEFT production_right RPRODUCTION'
        pass

    def p_production_right(self, p):
        '''production_right : LRIGHT VALUE RRIGHT
                    | LRIGHT empty RRIGHT
                    | RIGHT'''

    def p_empty(self, p):
        'empty :'
        pass

    # Error rule for syntax errors
    def p_error(self, p):
        if p:
            print("Syntax error at token", p.type)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        # else:
            # print("Syntax error at EOF")
