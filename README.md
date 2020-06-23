# Convertidor de multimedia :musical_score: :video_camera:

_Convertidor de formatos multimedia con un interfaz amigable para el usuario_

### Pre-requisitos 📋
Se necesita que en el computador tenga **Python** en la version 3.x [Descarga Python3.x](https://www.python.org/downloads/)

#### Instalar PIP
En este sitio estan los pasos con los enlaces a los programas correspondientes para cada sistema operativo
[Instalar PIP](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)


#### Instalar la libreria Pydub
```
pip install pydub
```
En caso de no saber si se tiene ingresar:
```
pydub -version
```
Con esta podrás ver la versión de pydub que este en tu ordenador

Para actualizar ingresa el siguiente comando
```
py -m pip install upgrade pip
```
o
```
python3 -m pip install upgrade pip
```

**Nota**: Si instalas python3 desde **Windows** lo mas probable es que lo lea con el comando **py** antes del programa a ejecutar. ejemplo:
```
py convert.py
```



#### Si usas Windows

**instalar ffmpeg** 

[Descarga ffmpeg](https://ffmpeg.zeranoe.com/builds/)

Nota: asegurarse de verificar la arquitectura del programa a descargar sea la misma de su ordenador (64x o 32x)

Una vez ya instalado, en variables del entorno agregar el PATH para ffmpeg
```
C:\FFmpeg\bin
```
más información de como hacerlo [instalar ffmpeg](https://www.solvetic.com/tutoriales/article/7976-como-instalar-ffmpeg-en-windows-10/)

En windows solo necesitas instalar el pydub y ffmpeg y podrás usar el programa



#### Si usas Linux
Te recomiendo que verifiques que en tu computador tengas instaladas las siguientes líbrerias

Si te sale un error donde se te indica que falta un decodificador h.264
instala con el siguiente comando
```
sudo apt-get install h264enc 
```
Para mas información de que hacer, aquí les dejó una página donde explica como hacerlo, si no funciona los comandos anteriores
[Mas información](https://ubuntu.dokry.com/12526/como-instalar-el-decodificador-h-264.html)

La libreria correspondiente
```
sudo apt install gstreamer1.0-libav
```

Instalar por pip
```
 pip install Avpy
```
para permitir la conversion a mp3

NOTA: El comando apt y apt-get son si usas una distribución de Debian o Ubuntu, este puede variar dependiendo la distribución que uses



### Instalación 🔧

Puedes clonar el repositorio con el comando 
```
git clone **El nombre del repositorio**
```
o Descargarlo como un archivo .ZIP 

Y para hacerlo correr, hay que ubicarse en el carpeta donde se encuentre el programa y solo tienes que ingresar

```
py convert.py
```
o
```
python3 convert.py
```




### Funcionamiento :open_file_folder:
#### Formatos
El programa permite convertir formatos multimedias como lo son:
```
Video
- .mp4

Audio
- .mp3
- .ogg
- .wav
```
#### Modo de Uso
El programa funciona ingresando el nombre completo del archivo con la extension incluida, se recomienda tener el archivo en la misma carpeta donde se encuentra el programa, pero en caso de no estarlo habrá que ingresar la ruta del archivo. y este se generara la conversión en dicha carpeta.

Si esta en Windows tiene que ir hasta la carpeta donde se encuentra el archivo, y copiar la que verá en la parte de arriba del explorador de archivos.

Si esta en Linux, puede ingresar el siguiente comando
```
pwd
```
Con esto podrá ver la ruta donde se encuentra en ese momento


## Este proyecto esta bajo la licencia (MIT) 
### mira el archivo [LICENSE](LICENSE) para mas detalles


