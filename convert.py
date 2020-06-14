from tkinter import *
from tkinter import ttk
from pydub import AudioSegment

# def mp3(url):
# 	song = AudioSegment.from_mp3(url)
# 	song.export('./'+url+'.ogg', format='ogg')


# def main():
	# print('C O N V E R T I R - A R C H I V O S')
	#url = str(input('Escriba el nombre del archivo, con las extension: '))
	#mp3(url)
	#enlace = '/home/andres/Documentos/challenge/python/convert_media/'
#
def interface():
	window = Tk()
	window.geometry('500x300')
	window.title('Convertidor de archivos')
	window.configure(bg='#2d2d2d')
	Label(window, text='Ingrese el nombre del archivo, con la extensión',bg='#2d2d2d',fg='#fff').pack(pady=15)
	url = StringVar()
	url_entry = Entry(window, textvariable=url, width=50, bg='beige').pack(pady=10)
	Button(window, text='Convertir', width=10, height=1).pack(pady=10)
	ttk.Button(window, text='Salir', command=window.destroy).pack(side=BOTTOM, pady=10)

	window.mainloop()




if __name__ =='__main__':
	interface()