import asyncio
from krakenbomber import AsyncBomber
from pyfiglet import figlet_format
async def main(phone,country_code):
	await AsyncBomber().send_spam(phone,country_code)
print("help for Developer. ton: UQAeAZH2DkWqsU8zLtdpx9ELkM0agCtCoi8myYkPOJ-9ObNS")
print(figlet_format("Kraken Bomber",font="5lineoblique"))
count=int(input("count threads»"))
phone=input("phone(without country code)»");country_code=input("country code(without +)»")
for x in range(count):
	asyncio.get_event_loop().run_until_complete(main(phone,country_code))