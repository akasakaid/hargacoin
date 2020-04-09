# CODED BY AKASAKAID
# 09/04/2020
# HIYA HIYA HIYA KAOWAWOAWKAWWA
import requests,json,time,sys,os
r = requests.Session()
def tunggu(t):
	while t:
		print(f"tunggu selama "+str(t)+f" detik untuk harga selanjutnya..",end='\r',flush=True)
		time.sleep(1)
		t -= 1
try:
	wk = int(input("Masukkan waktu jeda: "))
	if len(sys.argv) <2:
		print("cara menggunakan python nama.py nama_coin\ncontoh: python harga.py btc")
		exit()
	coin = sys.argv[1]
	if os.name == 'nt':os.system('cls')
	else:os.system('clear')
	print("""
MEMANTAU HARGA CRYPTOCOIN/UANG DIGITAL
POWERED BY PRO.COINBASE.COM
CODED BY AKASAKAID
""")
	while True:
		a = r.get('https://api.pro.coinbase.com/products/'+coin+'-usd/ticker').text
		if a == '{"message":"NotFound"}':
			print("coin tidak tersedia!!\nsilahkan coba coin yang lain")
			exit()
		else:
			b = json.loads(a)["price"]
			coin = coin.upper()
			print(f"Harga {coin}: {b} USD                                                 ")
			tunggu(wk)
except KeyboardInterrupt:
	print("keluar..")
	exit()
except Exception as e:
	print("error:",e)
