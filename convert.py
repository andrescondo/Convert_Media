from pydub import AudioSegment

def main():
	print('C O N V E R T I R - A R C H I V O S')
	url = str(input('Pegue el enlace del archivo a convertir: '))

	#enlace = '/home/andres/Documentos/challenge/python/convert_media/'

	song = AudioSegment.from_mp3(url)
	song.export('/home/andres/Documentos/challenge/python/convert_media/example.ogg', format='ogg')




if __name__ =='__main__':
	main()