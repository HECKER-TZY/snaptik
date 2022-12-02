#open source code
import time, os, requests, json, random, bs4
from rich.text import Text as tekz
from rich.panel import Panel as nel
from rich.panel import Panel
from rich.console import Console
xyz = requests.Session()
def logo():
  ban = """[green]by Irfan azhura[white]
╔═╗╔╗╔╔═╗╔═╗╔╦╗╦╦╔═  
╚═╗║║║╠═╣╠═╝ ║ ║╠╩╗  
╚═╝╝╚╝╩ ╩╩   ╩ ╩╩ ╩ """
  Console(width=50).print(Panel(ban,style='bold black'),justify='center')
  lol = """[white] Masukkan link url post tiktok yang ingin kamu dwonload!!!"""
  Console(width=50).print(Panel(lol,style='bold black'),justify='center')
path = "/storage/emulated/0/Download-video-tiktok"
try:
        os.mkdir(path)
except:
        pass
class Main:
	def __init__(self):
		pass
	def dow_tt(self, tk_vid, id_vid, nama_vid):
		nm_vid = f"tiktok_download_{nama_vid}"
		try:
			print (f' [•]Sedang Mendownload Video....')
			run = xyz.get(f'https://tikmate.app/download/{tk_vid}/{id_vid}.mp4?hd=1').content
			with open(f"{path}/{nm_vid}.mp4", "wb") as sv:
				sv.write(run)
				print (f' [•] Tersimpan di : {path}/{nm_vid}.mp4')
		except KeyError:
			exit(f' Url/Video erorr')
	def get_dat(self, url):
		data = {"url": url}
		try:
			data = requests.post('https://api.tikmate.app/api/lookup',data=data).text
			resp = json.loads(data)
			if 'true' in data:
				tk_vid = resp['token']
				id_vid = resp['id']
				at_vid = resp['author_name']
				tll_up_vid = resp['create_time']
				print (f' [•] Nama Creator   : {at_vid}')
				print (f' [•] id Video       : {id_vid}')
				print (f' [•] Tanggal Upload : {tll_up_vid}')
				dwon = input(f' [?] Inggin Download Video y/t: ')
				if dwon in ['Y','y']:
					nama_vid = input(f' [!] Masukan Nama untuk menyimpan video : ')
					self.dow_tt(tk_vid, id_vid, nama_vid)
				else:
					exit(f' memek!!!...')
			else:
				exit(f'Url/Video error')
		except KeyError:
			exit(f'Url/Video Error')
	def mulai(self):
		os.system("clear")
		logo()
		url = input(f' [!] Link : ')
		if url in ['']:
			exit(f' Link tidak di temukan' )
		else:
			self.get_dat(url)
Main().mulai()