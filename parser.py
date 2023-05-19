from lexer import lexer

def parser (src):
	print (" ")
	tokens = lexer(src)

	self = {
		'listTokens' : [i[0] for i in tokens] ,
		'index' : 0 ,
		'error' : False ,
		'sentenceDiagram' : [ ],
		'tokenInput' : " "
	}

	self['listTokens'].append('EOF') 

	if src == " ":
		print ("Cadena de entrada:", src, "(Cadena vacia)")
	else:
		print ("Cadena de entrada:", src)

	print ("tokens:", self['listTokens'])

	def parse ():
		#self['tokenInput'] = self['listTokens'][self['index']]
		#print("TokenInput: " + tokenInput)
		pni ('Programa')

		#print(self['error'], self['tokenInput'])

		if self['error'] == False and self['tokenInput'] == 'EOF':
			print("ARBOL DE DERIVACION:")
			self['sentenceDiagram'].reverse()
			for (symbol, right) in self['sentenceDiagram']:
				print (" ", symbol, " => ", right, " ")
			return True
		else:
			return False

	def pni (nonTerminalSymbol):
		for rightPart in productionRules[nonTerminalSymbol]:
			self['error'] = False
			i_pivote = self['index']

			#print ("Parte derecha de", nonTerminalSymbol, ":", rightPart)
			#print ("pivote de retroceso:", i_pivote)

			process (rightPart)

			if self['error'] == False:
				self['sentenceDiagram'].append((nonTerminalSymbol, rightPart))
				break
			elif self['error'] == True:
				self['index'] = i_pivote

	def process (rightPart):
		for s in rightPart:

			#print("index:",self['index'])
			#print (s, "es", funPruebas(s))
			#print(self['listTokens'],self['index'])
			
			self['tokenInput'] = self['listTokens'][self['index']]

			#print("token actual:", self['tokenInput'])
			#print(" ")

			if isTerminal (s):

				#print (s, "vs", self['tokenInput'])
				#print(" ")

				if s == self['tokenInput']:
					self['index'] += 1
				else:
					self['error'] = True
					break

			elif isNonTerminal (s):

				#print ("ingresa", s, "al pni?")
				#print(" ")

				pni (s)

				#print ("error:", self['error'])

				if self['error'] == True:
					break

	return parse ()

def isNonTerminal (ntSymbol):
	return ntSymbol in productionRules

def isTerminal (tSymbol):
	return not (isNonTerminal(tSymbol))

#def funPruebas (cad):
#	if isTerminal(cad):
#		return "terminal"
#	elif isNonTerminal(cad):
#		return "no terminal"

#def getSentenceDiagram(list_input):
#	list_input.reverse()
#	for (symbol, right) in list_input:
#		print (" " + symbol + " => " + right + " ")

productionRules = {

	'Programa' : [['ListaDecl', "EOF"]],
	
	'ListaDecl' : [['ListaDecl2']],
	
	'ListaDecl2' : [['Declaracion', 'ListaDecl2'], [ ]],
	
	'Declaracion' : [['FunDecl'], ['VarDecl'], ['Sentencia']],
	
	'FunDecl' : [["FUN", 'Funcion']],
	
	'Funcion' : [["ID", "(", 'ListaParametros', ")", 'Bloque']],
	
	'ListaParametros' : [['Parametros'], [ ]], #
	
	'Parametros' : [["ID", 'Parametros2']],
	
	'Parametros2' : [[",", "ID", 'Parametros2'], [ ]],
	
	'VarDecl' : [["VAR", "ID", ";"], ["VAR", "ID", "ALLOP", 'Expresion', ";"]],
	
	'Sentencia' : [['ExprSent'], ['ForSent'], ['IfSent'], ['ReturnSent'], ['WhileSent'], ['Bloque']],
	
	'ExprSent' : [['Expresion', ";"]],
	
	'Expresion' : [['Asignacion']],
	
	'Asignacion' : [["ID", "ALLOP", 'Primitivo'], ['OLogico']],
	
	'ForSent' : ["FOR", "(", 'PriArg', 'AdicArg', ";", 'AdicArg', ")", 'Sentencia'],
	
	'PriArg' : [['VarDecl'], ['ExprSent'], [";"]],	
	
	'AdicArg' : [['Expresion'], [ ]], #
	
	'IfSent' : [["IF", "(", 'Expresion', ")", 'Sentencia', "ELSE", 'Sentencia'], ["IF", "(", 'Expresion', ")", 'Sentencia']],
	
	'ReturnSent' : [["RETURN", 'Expresion', ";"], ["RETURN", ";"]],
	
	'WhileSent' : [["WHILE", "(", 'Expresion', ")", 'Sentencia']],
	
	'Bloque' : [["{", 'ListaDecl', "}"]],
	
	'OLogico' : [['YLogico'], ['YLogico', "LOGICOP", 'OLogico']],
	
	'YLogico' : [['Igua'], ['Igua', "LOGICOP", 'YLogico']],
	
	'Igua' : [['Comparacion'], ['Comparacion', "COMPOP", 'Igua']],
	
	'Comparacion' : [['Suma'], ['Suma', "COMPOP", 'Comparacion']],
	
	'Suma' : [['Mult'], ["ARITOP", 'Suma']],
	
	'Mult' : [['Unario'], ["ARITOP", 'Mult']],
	
	'Unario' : [["UNARY", 'Unario'], ['Primitivo']],
	
	'Primitivo' : [["TRUE"], ["FALSE"], ["NUMBER"], ["STRING"], ["ID"], ["(", 'Expresion', ")"]]
	
	}

#pruebas
print ("Pruebas del Parser")

test = [
	(" ", True),
	("fun contraataque ( casco ) { var pratto ; } perez = pratto ;", True),
	("fun motocloss ( scaloni , edul ) { }", True),
	("var sorny = 66 ;", True),
	("return maradona += 'pele' ;",	True),
	("while ( carter = reagan ) return bush = 'bush' ;", True),
	("funcion ( ) {[1,2,3]}", False),
	("for fun", False),
	("return 3", False),
	("else bolsonaro > dilma if { } ;", False),
	("fun (true, false)", False),
	("var var = 'georgeBest'", False)
	]

for (string, result) in test:
	assert parser (string) == result

