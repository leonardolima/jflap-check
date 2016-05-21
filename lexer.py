import ply.lex as lex

tokens = (
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
    'LTAG',             # <tag>
    'RTAG',             # </tag>
    'LWRITE',           # <write>
    'RWRITE',           # </write>
    'WRITE',            # <write/>
    'LMOVE',            # <move>
    'RMOVE',            # </move>
    'LPOP',             # <pop>
    'RPOP',             # </pop>
    'POP',              # <pop/>
    'LPUSH',            # <push>
    'RPUSH',            # </push>
    'PUSH',             # <push/>
    'LEXPRESSION',      # <expression>
    'REXPRESSION'       # </expression>
)

t_VALUE             = r'[0-9]+\.*[0-9]*|[a-z]+'
t_LSTRUCTURE        = r'<structure>'
t_RSTRUCTURE        = r'</structure>'
t_LTYPE             = r'<type>'
t_RTYPE             = r'</type>'
t_LAUTOMATON        = r'<automaton>'
t_RAUTOMATON        = r'</automaton>'
t_LSTATE            = r'<state.*>'
t_RSTATE            = r'</state>'
t_LX                = r'<x>'
t_RX                = r'</x>'
t_LY                = r'<y>'
t_RY                = r'</y>'
t_INITIAL           = r'<initial/>'
t_FINAL             = r'<final/>'
t_LTRANSITION       = r'<transition>'
t_RTRANSITION       = r'</transition>'
t_LFROM             = r'<from>'
t_RFROM             = r'</from>'
t_LTO               = r'<to>'
t_RTO               = r'</to>'
t_LREAD             = r'<read>'
t_RREAD             = r'</read>'
t_READ              = r'<read/>'
t_LPRODUCTION       = r'<production>'
t_RPRODUCTION       = r'</production>'
t_LLEFT             = r'<left>'
t_RLEFT             = r'</left>'
t_LRIGHT            = r'<right>'
t_RRIGHT            = r'</right>'
t_RIGHT             = r'<right/>'
t_LTRANSOUT         = r'<transout>'
t_RTRANSOUT         = r'</transout>'
t_LOUTPUT           = r'<output>'
t_ROUTPUT           = r'</output>'
t_LBLOCK            = r'<block>'
t_RBLOCK            = r'</block>'
t_LTAG              = r'<tag>'
t_RTAG              = r'</tag>'
t_LWRITE            = r'<write>'
t_RWRITE            = r'</write>'
t_LMOVE             = r'<move>'
t_RMOVE             = r'</move>'
t_LPOP              = r'<pop>'
t_RPOP              = r'</pop>'
t_POP               = r'<pop/>'
t_LPUSH             = r'<push>'
t_RPUSH             = r'</push>'
t_LEXPRESSION       = r'<expression>'
t_REXPRESSION       = r'</expression>'

t_ignore            = ' \t\n'
t_ignore_comment    = r'<!--.*-->'
t_ignore_version    = r'<\?.*\?>'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
