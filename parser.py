import lexer as l, ply.lex as lex, ply.yacc as yacc

class Parser(object):

    def __init__(self):
        self.tokens = l.tokens
        self.lexer = lex.lex(module=l)
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        self.parser.parse(data, tracking=True)
        # self.lexer.input(data)
        #
        # # Tokenize
        # while True:
        #     tok = self.lexer.token()
        #     if not tok:
        #         break      # No more input
        #     print(tok)

    def p_structure(self, p):
        '''structure : LSTRUCTURE LTYPE VALUE RTYPE body_fa RSTRUCTURE
                     | LSTRUCTURE LTYPE VALUE RTYPE body_tm RSTRUCTURE'''
        pass
    
    ## Types of body
    def p_body_fa(self, p):
        'body_fa : LAUTOMATON automaton_fa RAUTOMATON'
        pass

    def p_body_tm(self, p):
        'body_tm : LAUTOMATON automaton_tm machines RAUTOMATON'

    # Types of automaton
    def p_automaton_fa(self, p):
        '''automaton_fa : states transitions_fa'''
        pass

    def p_automaton_tm(self, p):
        '''automaton_tm : blocks transitions_tm'''
        pass

    # Representing states
    # FA: states
    # TM: blocks
    def p_states(self, p):
        '''states : state states
                  | empty'''
        pass

    def p_state(self, p):
        'state : LSTATE LX VALUE RX LY VALUE RY special output RSTATE'
        pass

    def p_blocks(self, p):
        '''blocks : block blocks
                  | empty'''
        pass

    def p_block(self, p):
        'block : LBLOCK LTAG VALUE RTAG LX VALUE RX LY VALUE RY special output RBLOCK'
        pass

    def p_special(self, p):
        '''special : INITIAL
                   | FINAL
                   | empty'''
        pass

    def p_state_output(self, p):
        '''output : LOUTPUT VALUE ROUTPUT
                  | empty'''
        pass

    # Transitions 
    # They differ according to the type of machine
    def p_transitions_fa(self, p):
        '''transitions_fa : transition_fa transitions_fa
                          | empty'''
        pass

    def p_transitions_tm(self, p):
        '''transitions_tm : transition_tm transitions_tm
                          | empty'''
        pass

    def p_transition_fa(self, p):
        # 'transition_fa : LTRANSITION LFROM NUM RFROM LTO NUM RTO read pop push transout write move RTRANSITION'
        'transition_fa : LTRANSITION LFROM VALUE RFROM LTO VALUE RTO READ RTRANSITION'
        pass

    def p_transition_tm(self, p):
        'transition_tm : LTRANSITION LFROM VALUE RFROM LTO VALUE RTO read write LMOVE VALUE RMOVE RTRANSITION'
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

    def p_machines(self, p):
        '''machines : machine machines
                    | empty'''
        pass

    def p_machine(self, p):
        'machine : LBRACKET VALUE SLASHRBRACKET'
        pass

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
            print ("Syntax error at token", p.type, "at position", p.lexpos)
            # Just discard the token and tell the parser it's okay.
            self.parser.errok()
        # else:
            # print("Syntax error at EOF")
