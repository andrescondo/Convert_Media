from tkinter import *
from tkinter import ttk
from pydub import AudioSegment


# def main():
	#url = str(input('Escriba el nombre del archivo, con las extension: '))
	#mp3(url)
	#enlace = '/home/andres/Documentos/challenge/python/convert_media/'
#
class Aplication():
	def __init__(self):
		self.window = Tk()
		self.window.geometry('500x200')
		self.window.title('Convertidor de archivos')
		self.window.configure(bg='#2d2d2d')

		#var
		url = StringVar(value='.mp3')

		#create label and entry
		self.eti1 = ttk.Label(self.window, text='Ingrese el nombre del archivo, con la extensión',bg='#2d2d2d',fg='#fff')
		self.text = ttk.Entry(self.window, textvariable=url, width=50, bg='beige')
		self.button1 = ttk.Button(self.window, text='Convertir', width=10, height=1)
		self.button2 = ttk.Button(self.window, text='Salir', command=self.window.destroy)

		#.pack()  
		self.eti1.pack(pady=15)
		self.text.pack(pady=10)
		self.button1.pack(pady=10)
		self.button2.pack(side=BOTTOM, pady=10)

		self.window.mainloop()


	# def mp3(url):
	# 	song = AudioSegment.from_mp3(url)
	# 	song.export('./'+url+'.ogg', format='ogg')



def main():
	my_app = Aplication()
	return 0


if __name__ =='__main__':
	main()


