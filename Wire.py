import os
import requests
from rich.console import Console
from rich.rule import Rule
import beaupy
import json
from dotenv import load_dotenv
load_dotenv()




BANNER = '''[magenta]
██╗    ██╗██╗██████╗ ███████╗
██║    ██║██║██╔══██╗██╔════╝
██║ █╗ ██║██║██████╔╝█████╗
██║███╗██║██║██╔══██╗██╔══╝
╚███╔███╔╝██║██║  ██║███████╗
╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚══════╝


by [green]https://github.com/therealOri[/green]

[/magenta]
'''



def clear():
	os.system("clear||cls")



def main():
	console = Console()
	console.print(BANNER)

	API_KEY = os.getenv("API_KEY")
	if not API_KEY:
		API_KEY = beaupy.prompt("Abstractapi Key - ( https://abstractapi.com ): ", secure=True)
		if not API_KEY:
			clear()
			quit()

	PHONE_NUMBER = beaupy.prompt("11 digit phone number - (14152007986): ")
	if not PHONE_NUMBER:
		clear()
		quit()

	url = f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={PHONE_NUMBER}"
	clear()

	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		console.rule(f"Results for number: '{PHONE_NUMBER}'\n")
		for key, value in data.items():
			key = key.replace("_", " ").title()
			console.print(f"[green][+][/green] {key}: {value}")
	else:
		clear()
		console.input(f'Unable to make request. Error code: [red]{response.status_code}[/red]\n\nPress "enter" to exit...')
		clear()
		quit()


if __name__ == '__main__':
	clear()
	main()
