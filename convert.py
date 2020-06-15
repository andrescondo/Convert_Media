from tkinter import *
from tkinter import ttk
from tkinter import messagebox #library for message
# from tkinter.ttk import Progressbar
from pydub import AudioSegment

#enlace = '/home/andres/Documentos/challenge/python/convert_media/example.mp3'

#
class Aplication():
	def __init__(self):
		self.window = Tk()
		self.window.geometry('600x200')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')

		#var
		self.url = StringVar()

		#create label and entry
		self.etiq1 = Label(self.window, text='Ingrese el nombre del archivo, con la extensión',bg='#2d2d2d',fg='#fff', font=("Arial",16))
		self.text = Entry(self.window, textvariable=self.url, width=70, bg='beige')
		self.button1 = Button(self.window, text='Convertir', width=10, height=1, command=self.mp4_wav)

		#bottom exit
		self.button2 = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#.pack()  
		self.etiq1.pack(pady=15)
		self.text.pack(pady=10)
		self.button1.pack(pady=10)
		self.button2.pack(side=BOTTOM, pady=10)

		self.window.mainloop()

#======================== AUDIO ============================================
	def mp3_ogg(self):
		url = self.url.get()
		song = AudioSegment.from_mp3(url)
		song.export('./'+url+'.ogg', format='ogg')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def ogg_mp3(self):
		url = self.url.get()
		song = AudioSegment.from_ogg(url)
		song.export('./'+url+'.mp3', format='.mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp3_wav(self):
		url = self.url.get()
		song = AudioSegment.from_wav(url)
		song.export('./'+url+'.wav', format='.wav')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def wav_mp3(self):
		url = self.url.get()
		song = AudioSegment.from_mp3(url)
		song.export('./'+url+'.mp3', format='.mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()


#========================= VIDEOS =======================================
	def mp4_mp3(self):
		url=self.url.get()
		video = AudioSegment.from_file(url, 'mp4')
		video.export('./'+url+'.mp3', format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp4_wav(self):
		url=self.url.get()
		video = AudioSegment.from_file(url, 'mp4')
		video.export('./'+url+'.wav', format='wav')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp4_flv(self):
		url=self.url.get()
		video = AudioSegment.from_file(url, 'mp4')
		video.export('./'+url+'.flv', format='flv')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def flv_mp4(self):
		url=self.url.get()
		video = AudioSegment.from_file(url, 'flv')
		video.export('./'+url+'.mp4', format='mp4')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def flv_mp3(self):
		url=self.url.get()
		video = AudioSegment.from_file(url, 'flv')
		video.export('./'+url+'.mp3', format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()
	






def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()