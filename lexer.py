import ply.lex as lex

states = (
    ('fa', 'inclusive'),
    ('pda', 'inclusive'),
    ('turing', 'inclusive'),
    ('grammar', 'inclusive'),
    ('lsystem', 'inclusive'),
    ('moore', 'inclusive'),
    ('mealy', 'inclusive'),
    ('re', 'inclusive')
)

tokens = (
    'LBRACKET',         # <
    'SLASHRBRACKET',    # />
    'VALUE',            # ".*"
    'LSTRUCTURE',       # <structure>
    'RSTRUCTURE',       # </structure>
    'LTYPE',            # <type>
    'RTYPE',            # </type>
    'LAUTOMATON',       # <automaton>
    'RAUTOMATON',       # </automaton>
    'LSTATE',           # <state>
    'RSTATE',           # </state>
    'LX',               # <x>
    'RX',               # </x>
    'LY',               # <y>
    'RY',               # </y>
    'INITIAL',          # <initial/>
    'FINAL',            # <final/>
    'LTRANSITION',      # <transition>
    'RTRANSITION',      # </transition>
    'LFROM',            # <from>
    'RFROM',            # </from>
    'LTO',              # <to>
    'RTO',              # </to>
    'LREAD',            # <read>
    'RREAD',            # </read>
    'READ',             # <read/>
    'LPRODUCTION',      # <production>
    'RPRODUCTION',      # </production>
    'LLEFT',            # <left>
    'RLEFT',            # </left>
    'LRIGHT',           # <right>
    'RRIGHT',           # </right>
    'RIGHT',            # <right/>
    'LTRANSOUT',        # <transout>
    'RTRANSOUT',        # </transout>
    'LOUTPUT',          # <output>
    'ROUTPUT',          # </output>
    'LBLOCK',           # <block>
    'RBLOCK',           # </block>
    'LCUSTOMBLOCK',
    'RCUSTOMBLOCK',
    'LTAG',             # <tag>
    'RTAG',             # </tag>
    'LWRITE',           # <write>
    'RWRITE',           # </write>
    'WRITE',            # <write/>
    'LMOVE',            # <move>
    'RMOVE',            # </move>
    'LTAPES',            # <tapes>
    'RTAPES',            # </tapes>
    'LPOP',             # <pop>
    'RPOP',             # </pop>
    'POP',              # <pop/>
    'LPUSH',            # <push>
    'RPUSH',            # </push>
    'PUSH',             # <push/>
    'LEXPRESSION',      # <expression>
    'REXPRESSION',      # </expression>
    'LAXIOM',           # <axiom>
    'RAXIOM',           # </axiom>
    'LPARAMETER',       # <parameter>
    'RPARAMETER',       # </parameter>
    'LNAME',            # <nane>
    'RNAME',            # </name>
    'LVALUE',           # <value>
    'RVALUE'            # </value>
)

# t_VALUE                                   = r'[0-9]+\.*[0-9]*|[0-9a-zA-Z]+' #FIXME
t_LSTRUCTURE                              = r'<structure>'
t_RSTRUCTURE                              = r'</structure>'
t_LTYPE                                   = r'<type>'
t_RTYPE                                   = r'</type>'
t_LBRACKET                                = r'<'
t_SLASHRBRACKET                           = r'/>'
t_fa_pda_turing_mealy_moore_LAUTOMATON        = r'<automaton>'
t_fa_pda_turing_mealy_moore_RAUTOMATON        = r'</automaton>'
t_fa_pda_turing_mealy_moore_LSTATE            = r'<state.*>'
t_fa_pda_turing_mealy_moore_RSTATE            = r'</state>'
t_fa_pda_turing_mealy_moore_LX                = r'<x>'
t_fa_pda_turing_mealy_moore_RX                = r'</x>'
t_fa_pda_turing_mealy_moore_LY                = r'<y>'
t_fa_pda_turing_mealy_moore_RY                = r'</y>'
t_fa_pda_turing_mealy_moore_INITIAL           = r'<initial[ ]*/>'
t_fa_pda_turing_mealy_moore_FINAL             = r'<final[ ]*/>'
t_fa_pda_turing_mealy_moore_LTRANSITION       = r'<transition[^>]*>'
t_fa_pda_turing_mealy_moore_RTRANSITION       = r'</transition>'
t_fa_pda_turing_mealy_moore_LFROM             = r'<from>'
t_fa_pda_turing_mealy_moore_RFROM             = r'</from>'
t_fa_pda_turing_mealy_moore_LTO               = r'<to>'
t_fa_pda_turing_mealy_moore_RTO               = r'</to>'
t_fa_pda_turing_mealy_moore_LREAD             = r'<read[^>]*>'
t_fa_pda_turing_mealy_moore_RREAD             = r'</read>'
t_fa_pda_turing_mealy_moore_READ              = r'<read[^>]*/>'
t_grammar_lsystem_LPRODUCTION                         = r'<production>'
t_grammar_lsystem_RPRODUCTION                         = r'</production>'
t_grammar_lsystem_LLEFT                               = r'<left>'
t_grammar_lsystem_RLEFT                               = r'</left>'
t_grammar_lsystem_LRIGHT                              = r'<right>'
t_grammar_lsystem_RRIGHT                              = r'</right>'
t_grammar_lsystem_RIGHT                               = r'<right/>'
t_moore_mealy_LTRANSOUT                       = r'<transout>'
t_moore_mealy_RTRANSOUT                       = r'</transout>'
t_moore_LOUTPUT                               = r'<output>'
t_moore_ROUTPUT                               = r'</output>'
t_turing_LBLOCK                               = r'<block[^>]*>'
t_turing_RBLOCK                               = r'</block>'
t_turing_LCUSTOMBLOCK                         = r'<.+\.jff[0-9]*>'
t_turing_RCUSTOMBLOCK                         = r'</.+\.jff[0-9]*>'
t_turing_LTAG                                 = r'<tag>'
t_turing_RTAG                                 = r'</tag>'
t_turing_LWRITE                               = r'<write[^>]*>'
t_turing_RWRITE                               = r'</write>'
t_turing_WRITE                                = r'<write[^>]*/>'
t_turing_LMOVE                                = r'<move[^>]*>'
t_turing_RMOVE                                = r'</move>'
t_turing_LTAPES                                = r'<tapes>'
t_turing_RTAPES                                = r'</tapes>'
t_pda_LPOP                                    = r'<pop>'
t_pda_RPOP                                    = r'</pop>'
t_pda_POP                                     = r'<pop/>'
t_pda_LPUSH                                   = r'<push>'
t_pda_RPUSH                                   = r'</push>'
t_pda_PUSH                                    = r'<push/>'
t_re_LEXPRESSION                              = r'<expression>'
t_re_REXPRESSION                              = r'</expression>'
t_lsystem_LAXIOM                              = r'<axiom>'
t_lsystem_RAXIOM                              = r'</axiom>'
t_lsystem_LPARAMETER                          = r'<parameter>'
t_lsystem_RPARAMETER                            = r'</parameter>'
t_lsystem_LNAME                                 = r'<name>'
t_lsystem_RNAME                                 = r'</name>'
t_lsystem_LVALUE                                = r'<value>'
t_lsystem_RVALUE                                = r'</value>'
t_ignore                                        = ' \t\r\n'
t_ignore_comment                                = r'<!--.*-->'
t_ignore_version                                = r'<\?xml.*\?>'
t_ignore_htmlcode                               = r'\&\#13;' # FIXME

def t_VALUE(t):
    r'(?<=>).+(?=</)|[A-Za-z0-9]+'
    for state, _ in states:
        if t.value == state:
            t.lexer.begin(state)
    return t

# Error handling rule
def t_ANY_error(t):
    print("Illegal character '%s'" % t.value[1])
    t.lexer.skip(1)
