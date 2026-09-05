# Copyright (c) 2026 FaraBro
# SPDX-License-Identifier: MIT OR Apache-2.0

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

class MorseCoder:
	@staticmethod
	def decode(obj: str) -> str:
		result = []
		for character in obj.split(' '):
			result.append(MORSE_DECODING_TABLE.get(character, '*'))
		
		return ''.join(result)
	
	@staticmethod
	def encode(obj: str) -> str:
		result = []
		obj = obj.lower()
		for character in obj:
			result.append(MORSE_ENCODING_TABLE.get(character, '') + ' ')
		
		return ''.join(result)

def main():
	def parse_args(list_of_args: list) -> dict:
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
			args['type'] = {'e': 'encode', 'encode': 'encode', 'd': 'decode', 'decode': 'decode'}.get(input("Задайте тип кодирования (encode (e)/decode (d)): ").lower())
			if args['type']:
				break
	
	funcForCoding = {'encode': MorseCoder.encode, 'decode': MorseCoder.decode}.get(args['type'], ValueError)
	if funcForCoding == ValueError:
		raise ValueError
	
	args['cycle'] = args.get('cycle', True)
	while True:
		in_data = args.get('in') if args.get('in') else input("> ")
		print(funcForCoding(in_data) + ('\n' if args['cycle'] else ''))
		if not args['cycle']:
			break

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(130)

"""
Код полная шняга
FIXME: Оно работает
"""
