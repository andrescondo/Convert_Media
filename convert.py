import os
import glob
from tkinter import *
from tkinter import ttk
from tkinter import messagebox #library for message
from pydub import AudioSegment
from tkinter import filedialog
from PIL import Image

class Aplication():
	def __init__(self):
		self.window = Tk()
		self.window.geometry('650x440')
		self.window.resizable(width=0, height=0)
		self.window.title('Manipulador de archivos de audio')
		#self.window.configure(bg='#2d2d2d')#, cursor='heart'		
		self.window['bg'] = '#2d2d2d'

		#var
		self.convert_3 = StringVar(value='NOMBRE.extensión')
		self.convert_w = StringVar(value='NOMBRE.extensión')
		self.edit = StringVar(value='NOMBRE.extensión')
		self.clase = StringVar(value='i')
		self.seg_record = DoubleVar(value=10)
		self.new_name = StringVar(value='Audio_Recortado')
		self.join_1 = StringVar(value='NOMBRE.extensión')
		self.join_2 = StringVar(value='NOMBRE.extensión')
		self.join_new = StringVar(value='NOMBRE.extensión')


		#self.img_url = PhotoImage(file='file.png')




		#create label and entry
		self.etiq1=Label(self.window,text='NOMBRE DEL ARCHIVO, O LA RUTA DONDE SE ENCUENTRA',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",15))
		# color celeste #b5deda  
		#==================
		self.tab_control = ttk.Notebook(self.window)

		#====================== box CONVERTIR ==================================
		self.tab1 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab1, text=' CONVERTIR ')
		
		self.labl1_1 = Label(self.tab1, text='Convertir a MP3',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text1_1 = Entry(self.tab1, textvariable=self.convert_3, width=80, bg='beige')
		self.button1_1 = Button(self.tab1, text='Convertir', width=10, height=1,bg='#A7A8A9', command=self.convert_mp3)

		self.labl1_3 = Label(self.tab1, text='Convertir a WAV',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text1_3 = Entry(self.tab1, textvariable=self.convert_w, width=80, bg='beige')
		self.button1_3 = Button(self.tab1, text='Convertir', width=10, height=1,bg='#A7A8A9', command=self.convert_wav)

		self.message = Label(self.tab1, text='Se pueden convertir los siguientes formatos: mp4, flv, ogg, mp3, wav',bg='#2d2d2d',fg='#fff')

		#====================== Edition ====================================
		self.tab2 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab2, text=' RECORTAR ')
		self.labl2_1 = Label(self.tab2, text='Ingrese el archivo que desea editar',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14) )
		self.text2_2 = Entry(self.tab2, textvariable=self.edit, width=80, bg='beige')
		self.labl2_3 = Label(self.tab2, text='Ingrese cuantos segundos desea recortar',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",10))
		self.text2_4 = Entry(self.tab2, textvariable=self.seg_record, width=10, bg='beige')
		self.clase1 = ttk.Radiobutton(self.tab2, text='Inicio',variable=self.clase, value='i')
		self.clase2 = ttk.Radiobutton(self.tab2, text='Final',variable=self.clase, value='f')
		self.labl2_5 = Label(self.tab2, text='Ingrese nuevo nombre',bg='#2d2d2d',fg='#fff',font=("Arial,Bold",10))
		self.text2_6 = Entry(self.tab2, textvariable=self.new_name, width=30, bg='beige')
		self.button_edit = Button(self.tab2, width=10,text='Recortar' ,bg='#A7A8A9' , command=self.cut_audio)

		#====================== Unir ====================================
		self.tab3 = ttk.Frame(self.tab_control)
		self.tab_control.add(self.tab3, text=' FUSIONAR ')
		self.labl3_1 = Label(self.tab3, text='Suba los audios que desea unir', bg='#2d2d2d',fg='#fff',font=("Arial,Bold",14))
		self.labl3_2 = Label(self.tab3, text='Primer audio', bg='#2d2d2d',fg='#fff',font=("Arial,Bold",10))
		self.text3_3 = Entry(self.tab3, textvariable=self.join_1,width=60, bg='beige')
		self.labl3_4 = Label(self.tab3, text='Segundo audio', bg='#2d2d2d',fg='#fff',font=("Arial,Bold",10))
		self.text3_5 = Entry(self.tab3, textvariable=self.join_2,width=60, bg='beige')
		self.labl3_6 = Label(self.tab3, text=' Ingrese el nombre del nuevo audio ', bg='#2d2d2d',fg='#fff',font=("Arial,Bold",10))
		self.text3_7 = Entry(self.tab3, textvariable=self.join_new,width=30, bg='beige')

		self.button_join = Button(self.tab3, width=10,text='Fusionar' ,bg='#A7A8A9', command=self.join_audio)
		#self.img = Button(self.tab3, image=self.img_url).pack()


		#self.file3_1
		#bottom exit
		self.button_exit = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#====.pack()=====================================  
		#Nota: sin el .pack() los elementos no serán visibles
		self.etiq1.pack(pady=15)


		#=== 1_# CONVERTIR
		self.labl1_1.pack(padx=40, pady=10, anchor='sw')
		self.text1_1.pack(pady=10)
		self.button1_1.pack(pady=10)

		self.labl1_3.pack(padx=40,pady=10, anchor='nw')
		self.text1_3.pack(pady=10)
		self.button1_3.pack(pady=10)

		self.message.pack(padx=30, pady=5, anchor='se')

		#=== 2_# EDICION
		self.labl2_1.pack(side=TOP, pady=10, padx=15, anchor="nw")
		self.text2_2.pack( pady=10, padx=15, anchor="nw")
		self.labl2_3.pack(side=TOP, pady=10, padx=15, anchor="nw")
		self.text2_4.pack( pady=5, padx=15, anchor="nw")
		self.clase1.pack(padx=50,pady=2,anchor="nw")
		self.clase2.pack(padx=50,pady=2,anchor="nw")
		self.labl2_5.pack(pady=5, padx=15,anchor="nw")
		self.text2_6.pack(side=LEFT, pady=5, padx=50,anchor="nw")
		self.button_edit.pack(side=BOTTOM,pady=5, padx=5, anchor="sw")

		#==== 3_# JOIN
		self.labl3_1.pack(padx= 10, pady=15, anchor="nw")
		self.labl3_2.pack(padx=15 , pady=5, anchor="nw")
		self.text3_3.pack(padx=15 , pady=5, anchor="nw")
		self.labl3_4.pack(padx=15 , pady=5, anchor="nw")
		self.text3_5.pack(padx=15 , pady=5, anchor="nw")
		self.labl3_6.pack(padx=15 , pady=5, anchor="nw")
		self.text3_7.pack(padx=15 , pady=5, anchor="nw")
		self.button_join.pack()

		
		self.button_exit.pack(side=BOTTOM,pady=10, padx=15, anchor="se")
		#self.lbl2.pack(pady=10)
		self.tab_control.pack(expand=1, fill='both')


		self.window.mainloop()

#======================== AUDIO ============================================
	def convert_mp3(self):
		try:
			url = self.convert_3.get()
			extension_list = ('*.wav','*.ogg')
			for extension in extension_list:
				mp3_filename = os.path.splitext(url)[0] + '.mp3'
			AudioSegment.from_file(url).export(mp3_filename, format='mp3')
		except FileNotFoundError:
			messagebox.showinfo('Fallo', 'El archivo que pusiste no existe, o el nombre esta incorrecto').pack()
			
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

	def convert_wav(self):
		try:
			url = self.convert_w.get()
			wav_filename = os.path.splitext(url)[0] + '.wav'
			AudioSegment.from_file(url).export(wav_filename, format='wav')
		except FileNotFoundError:
			messagebox.showinfo('Fallo', 'El archivo que pusiste no existe, o el nombre esta incorrecto').pack()

		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()

#====================== Cut =======================================
	def cut_audio(self):
		try:
			url = self.edit.get()
			seg = self.seg_record.get()
			name = str(self.new_name.get())
			time = (seg * 1000) + 1
			sound = AudioSegment.from_file(url)

			if self.clase.get() == 'i':
				sound_cut = sound[:time]

			elif self.clase.get() == 'f':
				sound_cut = sound[-time:]
			else:
				print('fallo')
		
			filename = os.path.splitext(name)[0]+ '.mp3'
			sound_cut.export(filename, format='mp3')
			messagebox.showinfo('Listo', 'El archivo ya fue recortado').pack()

		except FileNotFoundError:
			messagebox.showinfo('Fallo', 'El archivo que pusiste no existe, o el nombre esta incorrecto').pack()


#====================== JOIN =======================================
	def join_audio(self):
		try :
			audio_1 = self.join_1.get()
			audio_1 = AudioSegment.from_file(audio_1)
			audio_2 = self.join_2.get()
			audio_2 = AudioSegment.from_file(audio_2)
			join_n = str(self.join_new.get())

			if audio_1 != self.join_1 and audio_2 != self.join_2: 
				new_audio = audio_1 + audio_2
			else:
				messagebox.showinfo('Alto', 'Se deben ingresar dos audios').pack()

			filename = os.path.splitext(join_n)[0] + '.mp3'
			new_audio.export(filename, format='mp3')
			messagebox.showinfo('Listo', 'Se creo el nuevo audio').pack()

		except FileNotFoundError:
			messagebox.showinfo('Fallo', 'El archivo que pusiste no existe, o el nombre esta incorrecto').pack()
				
					


def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()