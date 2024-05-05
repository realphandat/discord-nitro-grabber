from requests import get
from random import choices
import string

class color:
	green = '\033[92m'
	red = '\033[91m'
	gray = '\033[90m'
	reset = '\033[0m'

def start():
	nitro = "".join(choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
	res = get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true")
	if res.status_code == 200:
		print(f"{color.green}[VALID]{color.reset} - https://discord.gift/{nitro}")
		with open("nitro.txt", "a") as f:
			f.write(f"https://discord.gift/{nitro}\n")
			f.close
	else:
		print(f"{color.red}[INVALID]{color.reset} - https://discord.gift/{nitro}")

while True:
	start()