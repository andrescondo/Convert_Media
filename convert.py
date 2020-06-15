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
		self.window.geometry('650x300')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')

		#var
		self.url = StringVar(value='.extensión')

		#create label and entry
		self.etiq1=Label(self.window,text='Ingrese el nombre del archivo, o la ruta donde se encuentra',bg='#2d2d2d',fg='#fff',font=("Arial",16))
		# color celeste #b5deda
		#==================
		self.tab_control = ttk.Notebook(self.window)
		self.tab1 = ttk.Frame(self.tab_control)
		self.tab2 = ttk.Frame(self.tab_control)

		#box Videos
		self.tab_control.add(self.tab1, text=' VIDEOS ')
		self.lbl1 = Label(self.tab1, text='Convertir de MP4 a WAV',bg='#2d2d2d',fg='#fff',font=("Arial",13) )

		self.text = Entry(self.tab1, textvariable=self.url, width=80, bg='beige')
		self.button1 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.mp4_wav)


		#box AUDIO
		self.tab_control.add(self.tab2, text=' AUDIO ')
		self.lbl2 = Label(self.tab2, text='')


		#bottom exit
		self.button2 = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#.pack()  
		self.etiq1.pack(pady=15)
		self.lbl1.pack(pady=10)
		self.text.pack(pady=10)
		self.button1.pack(pady=10)
		self.button2.pack(side=BOTTOM, pady=10)
		self.lbl2.pack(pady=10)
		self.tab_control.pack(expand=1, fill='both')

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