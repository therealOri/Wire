import requests
import sys
from rich.console import Console
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

os.system('clear||cls')
BANNER = '''[magenta]
          _)          
\ \  \   / |  __| _ \ 
 \ \  \ /  | |    __/ 
  \_/\_/  _|_|  \___| 

  
[green]by https://github.com/therealOri[/green]

[/magenta]
'''

console = Console()
console.print(BANNER)


arg = input('What phone number would you like to look up?: ')
os.system('clear||cls')


console.print(BANNER)
number = [arg[1:]]

for arg in number:
	console.rule(f'Results for number: \'{arg}\'')
	r = requests.get(API_URL.format(API_KEY, arg))
	
	if 'You do not have a valid API Key' in r.text:
		console.print('[red][-][/red] Your API Key is invalid')
		sys.exit()

	json_data = r.json()
	if json_data['valid'] == True:
		for key, value in json_data.items():
			if value:
				key = key.replace('_', ' ')

				if ' ' in key:
					x = key.split(' ')
					out = ''
					for y in x:
						out += y[0].upper() + y[1:] + ' '
					key = out
				else:
					key = key[0].upper() + key[1:]

				console.print(f'[green][+][/green] {key}: {value}')
	else:
		console.print('[red][-][/red] Invalid Phone Number.')
