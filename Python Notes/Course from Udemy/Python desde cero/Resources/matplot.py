#%%

#Aqui se importan matplotlib y numpy, numpy se importa solamente para poder
#Hacer graficos de ejemplo mas rapido, ya que nos permite hacer arrays con valores aleatorios en el array

import numpy as np
import matplotlib.pyplot as plt

#Sin hacer un array, osea con una lista, tambien se puede hacer, como vemos en este ejemplo
# Luego en la siguiente linea, se crea una instancia de un objeto tipo <matplotlib.lines.Line2D at 0x246160a9ee0>

#Estos objetos luego pueden ser interpretados con el metodo show, como veremos mas adelante en la linea 23

ahorros = [50, 10, 30, 65]
plt.plot(ahorros)

#
# %%
ahorros = np.random.randint(100, size = [12])
plt.plot(ahorros)
# %%
plt.plot(ahorros)
plt.show()
# %%
#Normalmente no podemos sustituir los numeros del array con letras pero esto podemos hacerlo, 
#Pasandole una lista de esta manera:

import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size = [6]) #>>>para seis meses
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))

#Ahora vamos a trabajar con los tres valores: ahorros, meses y mapeado:

plt.plot(ahorros)                       #Creamos el grafico
plt.xticks(mapeado, meses)              #Agregamos los valores horizontales

plt.show()                              #MOSTRAMOS EL GRAFICO

#El metodo xticks(los "ticks" para el eje X) lo que hace es que recibe dos argumentos, el primero
#Es un range, por tanto es una lista, un iterable, cuya longitud coincide con la de la lista de Ticks(meses)
# y ademas coincide con la longitu de la lista que usamos en el metodo plot


# %%
#Hasta ahora hemos decidido solamente cuales seran los valores del eje y, y dejado el eje x a incrementar,
#Pero tambien podemos elegir cuales son los valores que se van a mostrar en cada uno de los ejes.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(6)
y = np.random.randint(20, size=[6])

plt.plot(x, y) #>>>El primer valor es x, y el segundo valor es y
plt.show()

# %%
#Un dato importante y que vale la pena recordar es que una grafico que representa una funcion debe de ser
#Incremental ya que de no serlo la interpretacion del grafico sera una linea que se cruza, lo que no es conveniente 
#ni practico:

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y) #Ahora las lineas se cruzan porque la lista no es incremental, sino random
plt.show()

# %%
#LIMITES:

#Recordemos primero que todo que los limites que se establecen en el grafico se estableceran por default
#tomando en cuenta cuales son los limites inferior y superior de la lista que le hemos pasado, pero esto podemos
#Cambiarlo con los metodos xlim y ylim. Aunque normalmente se limita solo el eje y ya que para mejor comprension el eje x 
#debera de ser incremental en el tiempo.

import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size = [6]) #>>>para seis meses
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))


plt.plot(ahorros)
plt.ylim(0, 100)                      #Creamos el grafico
plt.xticks(mapeado, meses)              #Agregamos los valores horizontales
plt.show()
# %%
#Otros datos que vamos a querer mostrar en un grafico son, el titulo, y los nombres de los ejes, como meses y ahorros
#Esto se hace con los metodos siguientes:

#>>>plt.title("Ahorros del primer semestre") ----Para ek titulo 
#>>>plt.xlabel("Meses") ----para el label del eje x
#>>>plt.ylabel("Cantidad en $") ----para el label del eje y

#Otro aspecto a ver son las leyendas, en este caso el numero 4 hace referendia al "cuarto" cuadrante que es abajo a la derecha
#>>>plt.legend(4)

import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size = [6]) #>>>para seis meses
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))


plt.plot(ahorros, label = "Leyenda") #>>>Aqui es donde se establece el texo de la leyenda.
plt.ylim(0, 100)                      #Creamos el grafico
plt.xticks(mapeado, meses)              #Agregamos los valores horizontales
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en $")
plt.legend(loc=4)
plt.show()

#MAS SOBRE LA LEYENDA:
#---------------------

#La leyenda, como vemos es un texto, un label el cual curiosamente tiene una linea del mismo color de la linea del grafico,
#Esto es porque en un mismo grafico no tenemos que necesariamente tener solamnete una linea, podemos tener varias, para varios
#Usuarios por ejemplo, esto no es verdaderamente util para almacenar los datos o visualizarlos de manera individual,
#Sin embargo si queremos comparar tres individiuos, esta funcionalidad es bastante util.


# %%
#Uso de leyenda con mas usuarios:

import numpy as np
import matplotlib.pyplot as plt

mana_Kirito = np.random.randint(100, size = [6]) #>>>Para el usuario Kirito
mana_Alice = np.random.randint(100, size = [6]) #>>>Para el usuario Alice
mana_Eugeo = np.random.randint(100, size = [6]) #>>>Para el usuario Eugeo


meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))

#Ahora vamos a hacer las lineas de los arrays que creamos para cada usuario

plt.plot(mana_Kirito, label = "Kirito")
plt.plot(mana_Alice, label = "Alice")
plt.plot(mana_Eugeo, label = "Eugeo")

plt.ylim(0, 100)                      
plt.xticks(mapeado, meses)              
plt.title("Power increase")
plt.xlabel("Meses")
plt.ylabel("Cantidad de Mana")
plt.legend()   #Si le quitamos el loc, la leyenda se mostrara donde mejor se vea sin interferir con las lineas
plt.show()

# %%
#Por su puesto, todo el mundo sabe que el mana de Alice es amarillo, el de Kirito es negro y el de Eugeo es azul,
#asi que vamos a cambiar los colores y los estilos de estas lineas para que quede mejor:

import numpy as np
import matplotlib.pyplot as plt

mana_Kirito = np.random.randint(100, size =[6]) 
mana_Alice = np.random.randint(100, size = [6]) 
mana_Eugeo = np.random.randint(100, size = [6])


meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))

#Los colores de las lineas se cambian donde mismo se cambian las label, en la creacion del objeto plot:
#las propiedades son las siguientes:

#>>>color = "red" ---Puede ser un color en ingles o un color en Hx
#>>>ls = "-"      ---Esto es como sera la linea, corrida(-), intermitente (--), o intermitente con punto(-.)
#>>>lw = "4"      ---Este parametro significa line width, osea el ancho, no hay que explicarlo


plt.plot(mana_Kirito, label = "Kirito", color = "black", ls = "-", lw = "4")
plt.plot(mana_Alice, label = "Alice", color = "yellow", ls = "-", lw = "4")
plt.plot(mana_Eugeo, label = "Eugeo", color = "blue", ls = "--", lw = "4") #>>>Todo el mundo sabe porque la linea de Eugeo es intermitente :/

plt.ylim(0, 100)                      
plt.xticks(mapeado, meses)              
plt.title("Power increase")
plt.xlabel("Meses")
plt.ylabel("Cantidad de Mana")
plt.legend()   #Si le quitamos el loc, la leyenda se mostrara donde mejor se vea sin interferir con las lineas
plt.show()

#Para mas estilos de lineas simplemente visitamos la ducumentacion oficial.

# %%
#SUBGRAFICOS:
#------------

#De no querer los graficos en el mismo lugar simplemente dividimos la pantalla en tres, usando el metodo subplot:
#>>>plt.subplot(1, 3, 1) ---Esto significa, haz una tabla de una fila, un row, y tres columnas, y el tercer parametro es el lugar que ocupara ese 
#Grafico en la "Tabla". Despues de haber declarado esto simplemente creamos el plot que va a ir dentro de este sublopt como sigue:

import numpy as np
import matplotlib.pyplot as plt

mana_Kirito = np.random.randint(100, size =[6]) 
mana_Alice = np.random.randint(100, size = [6]) 
mana_Eugeo = np.random.randint(100, size = [6])


meses = ["E","F","M","A","M","J"] #>>>Solo podre letras porque hay poco espacio
mapeado = range(len(meses))

plt.subplot(1, 3, 1)

plt.plot(mana_Kirito, label = "Kirito", color = "black", ls = "-", lw = "4")
plt.ylim(0, 100)                      
plt.xticks(mapeado, meses)              
plt.title("Power increase")
plt.xlabel("Meses")
plt.ylabel("Cantidad de Mana")
plt.legend()


plt.subplot(1, 3, 2)

plt.plot(mana_Alice, label = "Alice", color = "yellow", ls = "-", lw = "4")
plt.ylim(0, 100)                      
plt.xticks(mapeado, meses)              
plt.title("Power increase")
plt.xlabel("Meses")
plt.ylabel("Cantidad de Mana")
plt.legend()


plt.subplot(1, 3, 3)

plt.plot(mana_Eugeo, label = "Eugeo", color = "blue", ls = "--", lw = "4") #:/
plt.ylim(0, 100)                      
plt.xticks(mapeado, meses)              
plt.title("Power increase")
plt.xlabel("Meses")
plt.ylabel("Cantidad de Mana")
plt.legend()

#At the end, we show, only once
plt.show()
# %%
#En el sguiente ejemplo vamos a automatiar la creacion de una tabla que contiene 9 graficos,
#En un cuadrado de 3x3 mediante un for:

for i in range(9):
    plt.subplot(3,3, i+1)
    plt.plot(np.random.randint(100, size =[6]) )
    plt.ylim(0,100)
plt.show()
