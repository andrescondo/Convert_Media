import os
import glob
from pydub import AudioSegment

#video_dir = '/home/andres/Documentos/challenge/python/convert_media/'  # Path where the videos are located
video_dir = str(input('INGRESE EL NOMBRE DEL ARCHIVO: '))
extension_list = ('*.mp4', '*.flv')

os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        mp3_filename = os.path.splitext(os.path.basename(video))[0] + '.mp3'
        AudioSegment.from_file(video).export(mp3_filename, format='mp3')