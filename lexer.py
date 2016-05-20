import ply.lex as lex

class Lexer(object):
	tokens = (
	'LBRACKET', # <
	'RBRACKET', # >
	'LSLASH',   # </
	'RSLASH',   # />
	'EQUALS',   # =
	'IDENT',    # [A-Za-z0-9.][A-Za-z0-9._]*
	'VALUE'		# ".*"
	)

	t_LBRACKET  		= r'<'
	t_RBRACKET  		= r'>'
	t_LSLASH    		= r'</'
	t_RSLASH    		= r'/>'
	t_EQUALS    		= r'='
	t_IDENT     		= r'[A-Za-z0-9.][A-Za-z0-9._]*'
	t_VALUE    			= r'"[0-9a-zA-Z]*"'
	t_ignore  			= ' \t\n'
	t_ignore_comment 	= r'<!--.*-->'
	t_ignore_version 	= r'<\?.*\?>'

	# Error handling rule
	def t_error(self, t):
		print("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	def __init__(self, **kwargs):
		self.lexer = lex.lex(module=self, **kwargs)

	def test(self, data):
		self.lexer.input(data)
		while True:
			tok = self.lexer.token()
			if not tok:
				break
			print(tok)
