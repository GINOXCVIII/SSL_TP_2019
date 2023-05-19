#---------------------------------------------------------------
#AUTOMATAS

TRAP_RESULT = "TRAP"
ACCEPT_RESULT = "ACCEPT"
NOACCEPT_RESULT = "NOT ACCEPT"
TRAP = -1

def number_Automaton (string):
	state = 0
	final_states = [1,3]
	for c in string:
		if state == 0 and c.isdigit():
			state = 1
		elif state == 1 and c.isdigit():
			state = 1
		elif state == 1 and c == ".":
			state = 2
		elif state == 2 and c.isdigit():
			state = 3
		elif state == 3 and c.isdigit():
			state = 3
		else:
			state = TRAP
			break
	if state == TRAP:
		return TRAP_RESULT
	if state in final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def string_Automaton (string):
	final_state = 3
	state = 0
	for c in string:
		if state == 0 and c == "'":
			state = 1
		elif state == 1 and (c.isdigit() or c.isalpha()):
			state = 2
		elif state == 2 and (c.isdigit() or c.isalpha()):
			state = 2
		elif state == 2 and c == "'":
			state = 3
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def ID_Automaton (string):
	state = 0
	final_state = 2
	for c in string:
		if state == 0 and c.isalpha():
			state = 1
		elif state == 1 and symbolList_Automaton(c) != NOACCEPT_RESULT:
			state = 2
		elif state == 2 and symbolList_Automaton(c) != NOACCEPT_RESULT:
			state = 2
		elif state == 1 and c == "_":
			state = 0
		elif state == 2 and c == "_":
			state = 0
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def digitList_Automaton (string):
	final_states = 1
	state = 0
	for c in string:
		if state == 0 and c.isdigit():
			state = 1
		elif state == 1 and c.isdigit():
			state = 1
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def symbolList_Automaton (string):
	final_state = 1
	state = 0
	for c in string:
		if state == 0 and (c.isdigit() or c.isalpha()):
			state = 1
		elif state == 1 and (c.isdigit() or c.isalpha()):
			state = 1
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def char_Automaton (string):
	state = 0
	final_state = 1
	for c in string:
		if state == 0 and c.isalpha():
			state = 1
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def digit_Automaton (string):
	final_state = 1
	state = 0
	for c in string:
		if state == 0 and c.isdigit():
			state = 1
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def logicalOperators_Automaton(string):
	if string in ["or", "and", "not"]:
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def arithmeticOperators_Automaton(string):
	state = 0
	final_state = 1
	if string == "**" or string == "//":
		state = 1
	elif string in ["+", "-", "*", "/", "%"]:
		state = 1
		#elif state == 1 and c in ["*", "/"]:  #contemplo la posibilidad de exponente y division entera
		#	state = 2

	else:
		state = TRAP

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def comparisonOperators_Automaton(string):
	state = 0
	final_state = 1

	if string in ["<", ">", "<=", ">=", "!=", "=="]:
		state = 1
	else:
		state = TRAP

	if state == TRAP:
		return TRAP_RESULT
	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def allocationOperators_automaton(string):
	state = 0
	final_state = 3

	if string == "=":
		state = 3
	else:
		for c in string:
			if state == 0 and c in ["+", "-", "*", "/"]:
				state = 1
			elif state == 0 and c == "=":
				state == 4
			#else:
			#	state = TRAP
			elif state == 1 and c == "=":
				state = 3
			elif state == 1 and c in ["*", "/"]:
				state = 2
			elif state == 2 and c == "=":
				state = 3

			else:
				state = TRAP
				break

	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT
		else:
			return TRAP_RESULT

##automatas para palabras reservadas

def if_Automaton(string):
	final_states = 2
	state = 0
	for c in string:
		if state == 0 and c == "i":
			state = 1
		elif state == 1 and c == "f":
			state = 2
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def for_Automaton(string):
	final_states = 3
	state = 0
	for c in string:
		if state == 0 and c == "f":
			state = 1
		elif state == 1 and c == "o":
			state = 2
		elif state == 2 and c == "r":
			state = 3
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def while_Automaton(string):
	final_states = 5
	state = 0
	for c in string:
		if state == 0 and c == "w":
			state = 1
		elif state == 1 and c == "h":
			state = 2
		elif state == 2 and c == "i":
			state = 3
		elif state == 3 and c == "l":
			state = 4
		elif state == 4 and c == "e":
			state = 5
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def else_Automaton(string):
	final_states = 4
	state = 0
	for c in string:
		if state == 0 and c == "e":
			state = 1
		elif state == 1 and c == "l":
			state = 2
		elif state == 2 and c == "s":
			state = 3
		elif state == 3 and c == "e":
			state = 4
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def return_Automaton(string):
	final_state = 6
	state = 0
	for c in string:
		if state == 0 and c == "r":
			state = 1
		elif state == 1 and c == "e":
			state = 2
		elif state == 2 and c == "t":
			state = 3
		elif state == 3 and c == "u":
			state = 4
		elif state == 4 and c == "r":
			state = 5
		elif state == 5 and c == "n":
			state = 6
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_state:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def eof_Automaton(string):
	final_states = 3
	state = 0
	for c in string:
		if state == 0 and c == "e":
			state = 1
		elif state == 1 and c == "o":
			state = 2
		elif state == 2 and c == "f":
			state = 3
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT
	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def fun_Automaton(string):
	final_states = 3
	state = 0
	for c in string:
		if state == 0 and c == "f":
			state = 1
		elif state == 1 and c == "u":
			state = 2
		elif state == 2 and c == "n":
			state = 3
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def in_Automaton(string):
	final_states = 2
	state = 0
	for c in string:
		if state == 0 and c == "i":
			state = 1
		elif state == 1 and c == "n":
			state = 2
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def var_Automaton(string):
	final_states = 3
	state = 0
	for c in string:
		if state == 0 and c == "v":
			state = 1
		elif state == 1 and c == "a":
			state = 2
		elif state == 2 and c == "r":
			state = 3
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def elif_Automaton(string):
	final_states = 4
	state = 0
	for c in string:
		if state == 0 and c == "e":
			state = 1
		elif state == 1 and c == "l":
			state = 2
		elif state == 2 and c == "i":
			state = 3
		elif state == 3 and c == "f":
			state = 4
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def true_Automaton(string):
	final_states = 4
	state = 0
	for c in string:
		if state == 0 and c == "t":
			state = 1
		elif state == 1 and c == "r":
			state = 2
		elif state == 2 and c == "u":
			state = 3
		elif state == 3 and c == "e":
			state = 4
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def false_Automaton(string):
	final_states = 5
	state = 0
	for c in string:
		if state == 0 and c == "f":
			state = 1
		elif state == 1 and c == "a":
			state = 2
		elif state == 2 and c == "l":
			state = 3
		elif state == 3 and c == "s":
			state = 4
		elif state == 4 and c == "e":
			state = 5
		else:
			state = TRAP
			break

	if state == TRAP:
		return TRAP_RESULT

	if state == final_states:
		return ACCEPT_RESULT
	else:
		if state != TRAP:
			return NOACCEPT_RESULT

def parOp_automaton(string):
	if string == "(":
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def braceOp_automaton(string):
	if string == "{":
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def braceCl_automaton(string):
	if string == "}":
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def parCl_automaton(string):
	if string == ")":
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def marks_automaton(string):
	if string == '"':
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def semicon_automaton(string):
	if string == ';':
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def coma_automaton(string):
	if string == ',':
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT

def unary_automaton(string):
	if string == '--' or string == '!':
		return ACCEPT_RESULT
	else:
		return TRAP_RESULT	

#---------------------------------------------------------------PROGRAMA_PRINCIPAL-------------------------------------------------------------#
def lexer(src): 
	tokens = []
	src = src + " " 
	i = 0
	start = 0
	state = 0
	while i < len(src):
		caracter = src[i]
		## si uso intervalos, tengo que sumarle 1 a i
		lexeme = src[start:i+1]
		
		if caracter.isspace(): 
			i += 1
			##ignoro el espacio y muevo el inicio 
			start = i
			#print("espacio")
		else:
			#lo uso solo para el error
			biggest_lexeme = src[start:i+1]
			##evaluo segun cada automata y avanzo hasta q sean trampa 
			while len(generateCandidates(lexeme)) != 0 and not caracter.isspace():
				i += 1
				state = 1
				lexeme = src[start:i+1]
				caracter = src[i]
				#print ("exitoso (por ahora)", lexeme,generateCandidates(lexeme))
				#lo uso solo para el error
				biggest_lexeme = lexeme
			i -= 1
			##retrocedo en la cadena
			lexeme = src[start:i+1]
			#print ("volver 1 atras", lexeme,generateCandidates(lexeme))
			##busco llegar a un estado aceptado
			while len(hasTrueCandidates(lexeme)) != 0 and len(lexeme) < 0:
				i -= 1
				lexeme = src[start:i+1]
				#print ("no encontre ninguno valido aun (por ahora)", lexeme, hasTrueCandidates(lexeme))
			##en este punto, tengo que tener al menos un valido, o una cadena vacia
			#print ("tengo 1 valido o el token no es reconocido", lexeme)
			lista_candidatos = hasTrueCandidates(lexeme)
			i += 1
			##si la lista de candidatos aceptados es vacia, tiro error
			if len(hasTrueCandidates(lexeme)) == 0:
				print("LEXEME NO RECONOCIDO EN POSICION "+str(i))
				tokens.append(('ERROR_TOKEN', biggest_lexeme))
				break
			else:
				##si tengo una lista de candidatos aceptados, tomo el primero
				token = lista_candidatos[0][0]
				tokens.append((token, lexeme))
				#print("TOKEN",token, lexeme)
				
			##marco el comienzo del lexeme nuevo	
			start = i
			state = 0
			biggest_lexeme = ''
	#print ("lexer run correct")
	#print("FIN")
	return(tokens)
	

def generateCandidates(string):
	candidates = []
	for (automaton, token) in RANK_TOKENS:
		if automaton(string) != TRAP_RESULT:
			candidates.append((token, string, automaton(string)))
	#print(candidates)
	return candidates

def hasTrueCandidates(string):
	trueCandidates = []
	for (automaton, token) in RANK_TOKENS:
		if automaton(string) == ACCEPT_RESULT:
			trueCandidates.append((token,string))
	return trueCandidates

##pruebas

RANK_TOKENS = [
	(eof_Automaton, 'EOF'), 
	(if_Automaton, 'IF'), 
	(elif_Automaton, 'ELIF'),
	(for_Automaton, 'FOR'), 
	(while_Automaton, 'WHILE'), 
	(else_Automaton, 'ELSE'), 
	(return_Automaton, 'RETURN'), 
	(fun_Automaton, 'FUN'), 
	(var_Automaton, 'VAR'), 
	(in_Automaton, 'IN'),
	(true_Automaton, 'TRUE'), 
	(false_Automaton, 'FALSE'), 
	(parOp_automaton, '('), 
	(parCl_automaton, ')'), 
	(braceOp_automaton, '{'),
	(braceCl_automaton, '}'),
	(marks_automaton, '"'), 
	(semicon_automaton, ';'), 
	(coma_automaton, ','),
	(logicalOperators_Automaton, 'LOGICOP'), 
	(allocationOperators_automaton, 'ALLOP'), 
	(comparisonOperators_Automaton, 'COMPOP'), 
	(arithmeticOperators_Automaton, 'ARITOP'), 
	(unary_automaton, 'UNARY'),
	(string_Automaton, 'STRING'), 
	(number_Automaton, 'NUMBER'), 
	(ID_Automaton, 'ID')]

	#(error_lexer, 'ERROR_TOKEN')

#print(lexer ("+="))
#print(allocationOperators_automaton("+="))
#print(allocationOperators_automaton("="))

#pruebas

cadenas = [
	"'probando'", 
	"probando con un for", 
	"me canse de escribir pruebas eof 'NDEAH'", 
	"if while else for return", 
	"'aloy' 12345 or", 
	"velvet and 'laphi'", 
	"333 + 333", 
	"for ) (", 
	"eofelse", 
	") (", 
	"musica_a_mi _ alrededor",
	"return maradona > pele"]

resultados_de_prueba = [
	[('STRING', "'probando'")], 
	[('ID', 'probando'), ('ID', 'con'), ('ID', 'un'), ('FOR', 'for')], 
	[('ID', 'me'), ('ID', 'canse'), ('ID', 'de'), ('ID', 'escribir'), ('ID', 'pruebas'), ('EOF', 'eof'), ('STRING', "'NDEAH'")], 
	[('IF', 'if'), ('WHILE', 'while'), ('ELSE', 'else'), ('FOR', 'for'), ('RETURN', 'return')], 
	[('STRING', "'aloy'"), ('NUMBER','12345'),('LOGICOP', 'or')],
	[('ID','velvet'), ('LOGICOP', 'and'), ('STRING', "'laphi'")], 
	[('NUMBER', '333'), ('ARITOP','+'), ('NUMBER', '333')], 
	[('FOR', 'for'), (')', ')'), ('(', '(')], 
	[('ID', 'eofelse')], 
	[(')', ')'), ('(', '(')], 
	[('ID', 'musica_a_mi'), ('ERROR_TOKEN', '_ ')],
	[('RETURN', 'return'), ('ID', 'maradona'), ('COMPOP', '>'), ('ID', 'pele')]] 


resultado0 = lexer(cadenas[0])
resultado1 = lexer(cadenas[1])
resultado2 = lexer(cadenas[2])
resultado3 = lexer(cadenas[3])
resultado4 = lexer(cadenas[4])
resultado5 = lexer(cadenas[5])
resultado6 = lexer(cadenas[6])
resultado7 = lexer(cadenas[7])
resultado8 = lexer(cadenas[8])
resultado9 = lexer(cadenas[9])
resultado10 = lexer(cadenas[10])
resultado11 = lexer(cadenas[11])
print('Las pruebas del lexer')
print('resultado 0: ',resultado0)
print('resultado 1: ',resultado1)
print('resultado 2: ',resultado2)
print('resultado 3: ',resultado3)
print('resultado 4: ',resultado4)
print('resultado 5: ',resultado5)
print('resultado 6: ',resultado6)
print('resultado 7: ',resultado7)
print('resultado 8: ',resultado8)
print('resultado 9: ',resultado9)
print('resultado 10: ',resultado10)
print('resultado 11: ',resultado11)
print(' ')
assert resultado0 == resultados_de_prueba[0]
assert resultado1 == resultados_de_prueba[1]
assert resultado2 == resultados_de_prueba[2]
assert resultado3 == resultados_de_prueba[3]
assert resultado4 == resultados_de_prueba[4]
assert resultado5 == resultados_de_prueba[5]
assert resultado6 == resultados_de_prueba[6]
assert resultado7 == resultados_de_prueba[7]
assert resultado8 == resultados_de_prueba[8]
assert resultado9 == resultados_de_prueba[9]
assert resultado10 == resultados_de_prueba[10]
assert resultado11 == resultados_de_prueba[11]

