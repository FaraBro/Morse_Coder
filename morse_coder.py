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
		for character in obj:
			try:
				result += MORSE_ENCODING_TABLE[character] + ' '
			except KeyError:
				continue
		
		return result


def main():
	type = (sys.argv[1].lower() if sys.argv[1].lower() in ['-e', '--encode', '-d', '--decode'] else None) if len(sys.argv) > 1 else None
	if type:
		type = type.lstrip('-')
	else:
		while True:
			type = input("Задайте тип кодирования (encode (e)/decode (d)): ").lower()
			if type in ['e', 'encode', 'decode', 'd']:
				break
	
	if type in ['encode', 'e']:
		type = 'encode'
		funcForCoding = morse_coder.encode
	elif type in ['decode', 'd']:
		type = 'decode'
		funcForCoding = morse_coder.decode
	else:
		raise ValueError
	
	while True:
		print(funcForCoding(input("> ").lower()) + '\n')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()

"""
Код полная шняга
FIXME: Работает, но непонятно почему. /j
"""
