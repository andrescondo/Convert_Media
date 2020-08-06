# Manipulador de multimedia a, Audio :musical_score: :video_camera:

_Manipulador de formatos multimedia a audio con un interfaz amigable para el usuario_

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

más información de como instarlo en: [instalar ffmpeg](https://www.solvetic.com/tutoriales/article/7976-como-instalar-ffmpeg-en-windows-10/)

Una vez ya instalado, en variables del entorno agregar el PATH para ffmpeg
```
C:\FFmpeg\bin
```


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
git clone https://github.com/andrescondo/Convert_Media.git
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
Esto depende en que sistema Operativo donde te encuentres, como tenga confidgurado Python en tu ordenador



### Funcionamiento :open_file_folder:
#### Formatos
El programa permite convertir formatos multimedias como lo son:
```
Video
- .mp4
- .flv

Audio
- .mp3
- .ogg
- .wav
```
#### Modo de Uso

##### Recortar

El programa funciona ingresando el nombre completo del archivo con la extension incluida, se recomienda tener el archivo en la misma carpeta donde se encuentra el programa, pero en caso de no estarlo habrá que ingresar la ruta del archivo. y este se generara la conversión en dicha carpeta.

Si estas en **Windows** puedes dar click derecho sobre el archivo y bajar entre las opciones, y eleguir la que dice 'Copiar como ruta de acceso', y obtendás la dirección completa del archivo. Otra opción es ir a la parte de arriba del explorador y dar doble click, hay se mostrará la ruta donde se encuentra la carpeta, y por consiguiente, donde esta el archivo.

Si esta en **Linux**, puede ingresar el siguiente comando
```
pwd
```


##### Edición

Al igual que con **Recortar**, para escoger el archivo se tiene que ingresar el nombre del archivo y la extensión, en caso de estar en la misma carpeta. Y en caso de estar en otra carpeta se tiene que ingresar ls ruta donde se encuentre el archivo, con el nombre y extensión del mismo.
Este viene con la caracteristica que se puede a un video recortar, pero igual mente se guardará como un audio (formato: .mp3)

Tambien hay que ingresar la cantdad en segundos que se desea recortar, en caso de que la cantidad sea mayor al tiempo del audio, este se guadará con el nuevo nombre y con el timepo del original.

Se podrá escoger que parte del video se desea recortar: **inicio, o final**.

Y en el último cuadro se podrá ingresar el nombre que se le dará al audio recortado, en caso de no poder nombre se guardará con el que esta por defecto, tener cuidado con esto, ya que el programa al guardar el archivo puede sobreescribirlo en caso de tener el mismo nombre.

##### Fusionar

Ahora el programa tiene un nuevo apartado en el que desde el se podrá unir dos diferentes músicas, solo ingresando los nombres y las respectivas extensiones, y con el ingreso de un nuevo nombre se tendrá un nueva música.


### Ejecutable

Enlace a [Mega](https://url2.cl/9Fv12)

El programa ahora cuenta con un ejecutable en Linux (Probado por el momento en ZorinOS), este se encuentra en un archivo comprimido **Ejecutable.zip**, y accediendo a la carpeta *Ejecutable linux*, y solo hay que darle doble click y se ejecutara el programa.

Para el Sistema operativo Windows, este se ejecuta así mismo ingresando a la carpeta comprimida **Ejecutable.zip**, y accediendo a la carpeta *Ejecutable Windows*, la única diferencia notoría sería el tiempo de ejecución, una vez dado el doble click se deberá esperar unos segundos para que el pograma comience a andar. 


### Recomendación

Suguiero que se descomprima el ejecutable para el SO correspondiente, y se posicione el ejecutable en el directorio donde se encuentren los archivos que se deseé manipular, de esta manera solo se tendrá que ingresar el nombre del archivo con su extensión.



## Este proyecto esta bajo la licencia (MIT) 
### mira el archivo [LICENSE](LICENSE) para mas detalles


