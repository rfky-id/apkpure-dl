# newbie
import os
import sys
import re
import requests
import bs4
import random

class apps(object):
	def __init__(self):
		self.s=requests.Session()
		self.dat=[]
		self.con=0
		self.counter=0
		self.ua={"User-Agent":"Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/7.0.55539 Mobile/12H321 Safari/600.1.4"}
		self.lirk()
		
	def randomize(self):
		self.up=[]
		fg=list("qwertyuiopasdfghjklzxcvbnm0123456789")
		for i in range(10):
			self.up.append(random.choice(fg))
		return "".join(self.up)

	def lirk(self):
		os.system("clear\necho [ ApkPure Downloader by Rfky-ID ]\necho")
		self.ly=raw_input("[*] search query: ").replace(" ","+").lower()
		if self.ly =="":
			self.lirk()
		self.fc()
		
	def fc(self):
		ft=bs4.BeautifulSoup(self.s.get("https://m.apkpure.com/id/search?q="+self.ly).text,features="html.parser")
		for i in ft.find_all("a",class_="dd"):
			try:
				self.con +=1
				kj=i.find("img")["title"]
				gt=i["href"]
				self.dat.append(gt)
				print("[%s] %s "%(self.con,kj)).lower()
			except:pass
		print
		self.choose()
	
	def choose(self):
		self.pen=int(raw_input("[*] Choice : "))
		if self.pen =="":
			self.choose()
		link=self.dat[self.pen-1]
		self.download("https://m.apkpure.com"+link)
		
	def download(self,link):
		random_=self.randomize()
		ft=bs4.BeautifulSoup(self.s.get(link).text,features="html.parser")
		kp=ft.find("a",class_="da")["href"]
		forsize=ft.find("span",class_="fsize")
		fort=re.findall(">(.*?)</h1>",str(ft))
		size=re.findall("an>(.*?)</span>",str(forsize))
		print("[+] Package Name : %s\n[+] File Size : %s"%(fort,size)).lower().replace("['","").replace("']","")
		with open(random_+".apk","wb") as k:
			afr=self.s.get("https://m.apkpure.com"+kp).text
			at=bs4.BeautifulSoup(afr,features="html.parser")
			ga = at.find("iframe",{"id":"iframe_download"})
			response = requests.get(ga["src"],stream=True,headers=self.ua)
			total=response.headers.get('content-length')
			if total is None:
				try:
					os.remove(random_+".apk")
				except:pass
				exit("[+] Downloading Fail!")
			else:
				total_csf=int(total)
				for data in response.iter_content(chunk_size=4096):
					fm=int(100*self.counter/total_csf)
					k.write(data)
					self.counter+=len(data)
					print("\r[%s] Downloading..."%(fm+1)),;sys.stdout.flush()
		print("\n[+] Download Success : %s"%(random_+".apk"))
			
apps()
