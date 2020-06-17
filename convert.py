import os
import glob
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
		self.window.geometry('650x600')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')#, cursor='heart'
		self.scrollbar = Scrollbar(self.window)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.mylist = Listbox(self.window, yscrollcommand=self.scrollbar.set )
		self.mylist.insert(END)
		self.scrollbar.config( command=self.mylist.yview )
		

		#var
		self.url = StringVar(value='.extensión')
		self.mp4_3 = StringVar(value='.extensión')
		self.mp4_w = StringVar(value='.extensión')
		self.mp4_f = StringVar(value='.extensión')
		self.flv_3 = StringVar(value='.extensión')
		self.flv_4 = StringVar(value='.extensión')

		#create label and entry
		self.etiq1=Label(self.window,text='Ingrese el nombre del archivo, o la ruta donde se encuentra',bg='#2d2d2d',fg='#fff',font=("Arial",16))
		# color celeste #b5deda
		#==================
		self.tab_control = ttk.Notebook(self.window)

		#box Videos
		self.tab1 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab1, text=' VIDEOS ')

		#mp4 a mp3
		self.labl2 = Label(self.tab1, text='Convertir de MP4 o FLV, a MP3',bg='#2d2d2d',fg='#fff',font=("Arial",14) )
		self.text2 = Entry(self.tab1, textvariable=self.mp4_3, width=80, bg='beige')
		self.button_2 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.video_mp3)

		#mp4 a flv
		self.labl3 = Label(self.tab1, text='Convertir de MP4 a FLV',bg='#2d2d2d',fg='#fff',font=("Arial",14) )
		self.text3 = Entry(self.tab1, textvariable=self.mp4_f, width=80, bg='beige')
		self.button3 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.mp4_flv)

		#====================== box AUDIO ==================================
		self.tab2 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab2, text=' AUDIO ')
		self.lbl2 = Label(self.tab2, text='')


		#bottom exit
		self.button_exit = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#====.pack()  
		self.etiq1.pack(pady=15)

		self.labl2.pack(pady=10)
		self.text2.pack(pady=10)
		self.button_2.pack(pady=10)

		self.labl3.pack(pady=10)
		self.text3.pack(pady=10)
		self.button3.pack(pady=10)
		
		self.button_exit.pack(side=BOTTOM,pady=10)
		self.lbl2.pack(pady=10)
		self.tab_control.pack(expand=1, fill='both')


		#self.window.config(menu=self.menu)
		self.window.mainloop()

#======================== AUDIO ============================================
	def mp3_ogg(self):
		url = self.mp3_o.get()
		song = AudioSegment.from_mp3(url)
		song.export('./'+url+'.ogg', format='ogg')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def ogg_mp3(self):
		url = self.ogg_3.get()
		song = AudioSegment.from_ogg(url)
		song.export('./'+url+'.mp3', format='.mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp3_wav(self):
		url = self.mp3_w.get()
		song = AudioSegment.from_wav(url)
		song.export('./'+url+'.wav', format='.wav')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def wav_mp3(self):
		url = self.wav_3.get()
		song = AudioSegment.from_mp3(url)
		song.export('./'+url+'.mp3', format='.mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()


#========================= VIDEOS =======================================
	def video_mp3(self):
		url=self.mp4_3.get()
		extension_list = ('*.mp4', '*.flv')

		for extension in extension_list:
			mp3_filename = os.path.splitext(url)[0] + '.mp3'
			AudioSegment.from_file(url).export(mp3_filename, format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	# def mp4_wav(self):
	# 	url=self.mp4_w.get()
	# 	video = AudioSegment.from_file(url, 'mp4')
	# 	video.export('./'+url+'.wav', format='wav')
	# 	messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp4_flv(self):
		url=self.mp4_f.get()
		video = AudioSegment.from_file(url, 'mp4')
		video.export('./'+url+'.flv', format='flv')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def flv_mp4(self):
		url=self.flv_4.get()
		video = AudioSegment.from_file(url, 'flv')
		video.export('./'+url+'.mp4', format='mp4')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()



def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()