from tkinter import *
from tkinter import ttk
from tkinter import messagebox #library for message
from pydub import AudioSegment

#enlace = '/home/andres/Documentos/challenge/python/convert_media/example.mp3'

#
class Aplication():
	def __init__(self):
		self.window = Tk()
		self.window.geometry('500x200')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')

		#var
		self.url = StringVar(value='.mp3')

		#create label and entry
		self.etiq1 = Label(self.window, text='Ingrese el nombre del archivo, con la extensión',bg='#2d2d2d',fg='#fff')


		self.text = Entry(self.window, textvariable=self.url, width=50, bg='beige')
		self.button1 = Button(self.window, text='Convertir', width=10, height=1, command=self.mp4)

		#bottom exit
		self.button2 = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#.pack()  
		self.etiq1.pack(pady=15)
		self.text.pack(pady=10)
		self.button1.pack(pady=10)
		self.button2.pack(side=BOTTOM, pady=10)

		self.window.mainloop()


	def mp3(self):
		url = self.url.get()

		song = AudioSegment.from_mp3(url)
		song.export('./'+url+'.ogg', format='ogg')

	def mp4(self):
		url=self.url.get()

		ex_video = AudioSegment.from_file(url, 'mp4')
		ex_video.export('./'+url+'.mp3', format='mp3')
		messagebox.showinfo('Listo', 'El archivo ya esta convertido').pack()




def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()