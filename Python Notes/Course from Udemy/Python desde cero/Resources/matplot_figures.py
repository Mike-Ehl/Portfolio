#%%
#Existe una mejor forma de trabajar con estos graficos, una forma que nos permite cambiar mas settings, y personalizar mas el grafico
#esto se logra creando una instancia de la clase figura, son este objeto es con lo que vamos a comenzar:

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure() #>>>Instancia de la clase figura del modulo plt, del paquete matplotlib

#Despues de esto vamos a crear una variable que es una tupla que es la que hace referencia a los ejes

rect = (0,0,1,1)
axes = fig.add_axes(rect) #>>>Aqui a la instancia figura se le aplica el metodo add_axes, y a este se le pasa la variable guardando los axes que creamos
#Pero porque simplemente no creamos el axes y le pasamosla tupla, bueno, tener esto guardado en una variable hace que podamos asignarle una nueva

#Ahora creamos nuestros arrays que son la base de nuestros graficos:

mana_Kirito = np.random.randint(100, size =[6]) 
mana_Alice = np.random.randint(100, size = [6]) 
mana_Eugeo = np.random.randint(100, size = [6])

#Y con estos graficos creados podemos entonces pasarselos como argumento de nuestro metodo plot, aunque esta vez
#El metodo no sera ejecutado sobre el plot, que era el unico objeto que teniamos, sino que sera ejecutado sobre axes, que son los ejes para este objeto
#figura en particular.

axes.plot(mana_Kirito, label = "Kirito", color = "black")
axes.plot(mana_Alice, label = "Alice", color = "yellow")
axes.plot(mana_Eugeo, label = "Eugeo", color = "blue")

#Aqui los limites se le establecen al propio axes, quien pare ser el main object de esta manera de hacer graficos
#Lo mismo sucede con los titulos, labels de los ejes y los ticks, si  aqui si es mas facil modificar los ticks

axes.set_ylim(0, 100)
axes.set_ylabel("Cantidad de Mana")
axes.set_xlabel("Meses")
axes.set_title("Power Increase")

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"] #>>> Creamos una lista de meses para usar en los ticks
mapeado = range(len(meses)) #>>>Asi como tabien el respectivo mapeado

axes.set_xticks(mapeado)#>>>Aqui de hecho lo que se agrega no son los meses, sino que cantidad de meses hay, asi como un valor numerico por tick, debido al range
axes.set_xticklabels(meses)
axes.legend()

#Finalmente Mostramos con show

fig.show()
# %%
#La mejora aqui esta en que podemos de hecho cambiar la calidad del objeto de salida:



import numpy as np
import matplotlib.pyplot as plt

#La calidad del grafico se cambia en la creacion del propio objeto figure, cambiando si resolicion, largo y ancho, y du densidad de pixeles por inch o "dpi"

fig = plt.figure(figsize=(4,2), dpi = 300) #>>>dpi es lo que realmente cambia la calidad
rect = (0,0,1,1)
axes = fig.add_axes(rect)
mana_Kirito = np.random.randint(100, size =[6]) 
mana_Alice = np.random.randint(100, size = [6]) 
mana_Eugeo = np.random.randint(100, size = [6])
axes.plot(mana_Kirito, label = "Kirito", color = "black")
axes.plot(mana_Alice, label = "Alice", color = "yellow")
axes.plot(mana_Eugeo, label = "Eugeo", color = "blue")
axes.set_ylim(0, 100)
axes.set_ylabel("Cantidad de Mana")
axes.set_xlabel("Meses")
axes.set_title("Power Increase")
meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio"]
mapeado = range(len(meses))
axes.set_xticks(mapeado)
axes.set_xticklabels(meses)
axes.legend()

fig.show()