import sys

MORSE_DECODING_TABLE = {
	'.-': 'а',
	'-...': 'б',
	'.--': 'в',
	'--.': 'г',
	'-..': 'д',
	'.': 'е',
	'...-': 'ж',
	'--..': 'з',
	'..': 'и',
	'.---': 'й',
	'-.-': 'к',
	'.-..': 'л',
	'--': 'м',
	'-.': 'н',
	'---': 'о',
	'.--.': 'п',
	'.-.': 'р',
	'...': 'с',
	'-': 'т',
	'..-': 'у',
	'..-.': 'ф',
	'....': 'х',
	'-.-.': 'ц',
	'---.': 'ч',
	'----': 'ш',
	'--.-': 'щ',
	'--.--': 'ъ',
	'-.--': 'ы',
	'-..-': 'ь',
	'..-..': 'э',
	'..--': 'ю',
	'.-.-': 'я',
	'-----': '0',
	'.----': '1',
	'..---': '2',
	'...--': '3',
	'....-': '4',
	'.....': '5',
	'-....': '6',
	'--...': '7',
	'---..': '8',
	'----.': '9',
	'.-.-.-': '.',
	'--..--': ',',
	'..--..': '?',
	'-.-.--': '!',
	'-...-': '`',
	'-.--.': '(',
	'-.--.-': ')',
	'-..-.': '/',
	'.-...': '&',
	'---...': ':',
	'-.-.-.': ';',
	'-...-': '=',
	'.-.-.': '+',
	'-....-': '-',
	'.-..-.': '"',
	'.--.-.': '@',
	'...-.-': 'конец связи',
	'/': ' ',
}
MORSE_ENCODING_TABLE = {value: key for key, value in MORSE_DECODING_TABLE.items()}

class morse_coder:
	@staticmethod
	def decode(obj: str):
		result = ""
		for character in obj.split(' '):
			try:
				result += MORSE_DECODING_TABLE[character]
			except KeyError:
				result += '*'
				continue
		
		return result
	
	@staticmethod
	def encode(obj: str):
		result = ""
		obj = obj.lower()
		for character in obj:
			try:
				result += MORSE_ENCODING_TABLE[character] + ' '
			except KeyError:
				continue
		
		return result

def main():
	def parse_args(list_of_args: list):
		args = {}
		in_arg = False
		for arg in list_of_args:
			if in_arg:
				args['in'] = arg
				in_arg = False
			else:
				arg = arg.lower()
				if arg in ['-e', '--encode']:
					args['type'] = 'encode'
				elif arg in ['-d', '--decode']:
					args['type'] = 'decode'
				elif arg in ['-or', '--only_result']: # Да, да.. or.... Это на будущее.
					args['only_result'] = True
				elif arg in ['-i', '--in']:
					args['cycle'] = False
					in_arg = True
					continue
				elif arg in ['-nc', '--no_cycle']:
					args['cycle'] = False
		
		return args
	
	args = parse_args(sys.argv)
	if not args.get('type'):
		while True:
			args['type'] = input("Задайте тип кодирования (encode (e)/decode (d)): ").lower()
			if args['type'] in ['e', 'encode', 'decode', 'd']:
				break
	
	funcForCoding = morse_coder.encode if args['type'] == 'encode' else (morse_coder.decode if args['type'] == 'decode' else ValueError)
	if funcForCoding == ValueError:
		raise ValueError
	
	if args.get('cycle') == None:
		args['cycle'] = True
	while True:
		in_data = args.get('in') if args.get('in') else input("> ")
		print(funcForCoding(in_data) + ('\n' if args['cycle'] else ''))
		if not args['cycle']:
			break

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()

"""
Код полная шняга
FIXME: Оно работает
"""
