import os
import glob
from tkinter import *
from tkinter import ttk
from tkinter import messagebox #library for message
from pydub import AudioSegment

class Aplication():
	def __init__(self):
		self.window = Tk()
		self.window.geometry('650x600')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')#, cursor='heart'		

		#var
		self.video_3 = StringVar(value='NOMBRE.extensión')
		self.mp4_f = StringVar(value='NOMBRE.extensión')
		self.flv_4 = StringVar(value='NOMBRE.extensión')
		self.audio_3 = StringVar(value='NOMBRE.extensión')
		self.mp3_o = StringVar(value='NOMBRE.extensión')
		self.mp3_w = StringVar(value='NOMBRE.extensión')


		#create label and entry
		self.etiq1=Label(self.window,text='NOMBRE DEL ARCHIVO, O LA RUTA DONDE SE ENCUENTRA',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",15))
		# color celeste #b5deda  
		#==================
		self.tab_control = ttk.Notebook(self.window)

		#========================== box Videos ==========================
		self.tab1 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab1, text=' VIDEOS ')

		self.labl1_1 = Label(self.tab1, text='Convertir de MP4 o FLV, a MP3',bg='#2d2d2d',fg='#fff',font=("Arial ,Bold",14) )
		self.text1_1 = Entry(self.tab1, textvariable=self.video_3, width=80, bg='beige')
		self.button1_1 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.video_mp3)

		self.labl1_2 = Label(self.tab1, text='Convertir de MP4 a FLV',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text1_2 = Entry(self.tab1, textvariable=self.mp4_f, width=80, bg='beige')
		self.button1_2 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.mp4_flv)

		self.labl1_3 = Label(self.tab1, text='Convertir de FLV a MP4',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text1_3 = Entry(self.tab1, textvariable=self.flv_4, width=80, bg='beige')
		self.button1_3 = Button(self.tab1, text='Convertir', width=10, height=1, command=self.flv_mp4)

		#====================== box AUDIO ==================================
		self.tab2 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab2, text=' AUDIO ')
		
		self.labl2_1 = Label(self.tab2, text='Convertir de OGG o WAV a MP3',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text2_1 = Entry(self.tab2, textvariable=self.audio_3, width=80, bg='beige')
		self.button2_1 = Button(self.tab2, text='Convertir', width=10, height=1, command=self.audio_mp3)

		self.labl2_2 = Label(self.tab2, text='Convertir de MP3 a OGG',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text2_2 = Entry(self.tab2, textvariable=self.mp3_o, width=80, bg='beige')
		self.button2_2 = Button(self.tab2, text='Convertir', width=10, height=1, command=self.mp3_ogg)

		self.labl2_3 = Label(self.tab2, text='Convertir de MP3 a WAV',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text2_3 = Entry(self.tab2, textvariable=self.mp3_w, width=80, bg='beige')
		self.button2_3 = Button(self.tab2, text='Convertir', width=10, height=1, command=self.mp3_wav)

		#bottom exit
		self.button_exit = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#====.pack()=====================================  
		#Nota: sin el .pack() los elementos no serán visibles
		self.etiq1.pack(pady=15)

		#=== 1_# VIDEO
		self.labl1_1.pack(pady=10)
		self.text1_1.pack(pady=10)
		self.button1_1.pack(pady=10)
		#--------
		self.labl1_2.pack(pady=10)
		self.text1_2.pack(pady=10)
		self.button1_2.pack(pady=10)
		#--------
		self.labl1_3.pack(pady=10)
		self.text1_3.pack(pady=10)
		self.button1_3.pack(pady=10)

		#=== 2_# AUDIO
		self.labl2_1.pack(pady=10)
		self.text2_1.pack(pady=10)
		self.button2_1.pack(pady=10)

		self.labl2_2.pack(pady=10)
		self.text2_2.pack(pady=10)
		self.button2_2.pack(pady=10)

		self.labl2_3.pack(pady=10)
		self.text2_3.pack(pady=10)
		self.button2_3.pack(pady=10)
		
		self.button_exit.pack(side=BOTTOM,pady=10)
		#self.lbl2.pack(pady=10)
		self.tab_control.pack(expand=1, fill='both')


		#self.window.config(menu=self.menu)
		self.window.mainloop()

#======================== AUDIO ============================================
	def mp3_ogg(self):
		url = self.mp3_o.get()
		ogg_filename = os.path.splitext(url)[0] + '.ogg'
		AudioSegment.from_file(url).export(ogg_filename, format='ogg')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def audio_mp3(self):
		url = self.audio_3.get()
		extension_list = ('*.wav','*.ogg')
		for extension in extension_list:
			mp3_filename = os.path.splitext(url)[0] + '.mp3'
			AudioSegment.from_file(url).export(mp3_filename, format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp3_wav(self):
		url = self.mp3_w.get()
		wav_filename = os.path.splitext(url)[0] + '.wav'
		AudioSegment.from_file(url).export(wav_filename, format='wav')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()


#========================= VIDEOS =======================================
	def video_mp3(self):
		url=self.video_3.get()
		extension_list = ('*.mp4', '*.flv')

		for extension in extension_list:
			mp3_filename = os.path.splitext(url)[0] + '.mp3'
			AudioSegment.from_file(url).export(mp3_filename, format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def mp4_flv(self):
		url=self.mp4_f.get()
		flv_filename = os.path.splitext(url)[0] + '.flv'
		AudioSegment.from_file(url, 'flv').export(flv_filename, format='flv')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def flv_mp4(self):
		url=self.flv_4.get()
		mp4_filename = os.path.splitext(url)[0] + '.mp4'
		AudioSegment.from_file(url).export(mp4_filename, format='mp4')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()



def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()