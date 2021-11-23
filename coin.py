import samino
from threading import Thread

client = samino.Client("22FCB673B848DDD4AD7869E3B374AD3CCE884F8D631C027AE596EC7D614638785015596A6F61A2E3AE")

counter = 0

for ulink in open("urls.txt").read().split():
	uid=client.get_from_link(ulink).objectId
	for _ in range(25):
		client.watch_ad(uid)
		print(f"LUFFY FARMOU: {_}")
	counter+=1
	print(f"LUFFY FEZ DE NOVO EM: {1}")
