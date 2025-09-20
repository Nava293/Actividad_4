#Importar 'randrange' de la biblioteca random para generar las coordenadas aleatorias
from random import randrange
#Importar todos los elementos de la biblioteca visual turtle
from turtle import *
#Importar los vectores para movimiento de 'freegames'
from freegames import vector

#Definir el proyectil 'ball' en el punto inicial, la esquina inferior izquierda de la pantalla
ball = vector(-200, -200)
#Definir la velocidad como cero para luego cambiarla por el valor dado al dar clic
speed = vector(0, 0)
#Matriz donde se almacenarán todos los objetivos
targets = []

#Función para definir lo que pasa cuando se hace clic en pantalla
def tap(x, y):
    #Primero determina que el proyectil no se encuentre en pantalla, que es su posición inicial y para evitar varios proyectiles en pantalla
    if not inside(ball):
        #Si determina que no hay ninguno en pantalla, permite que se desplace a la parte visible
        ball.x = -199
        ball.y = -199
        #Determina la velocidad del proyectil según las coordenadas donde se generaron los clics
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
        speed.x = (x + 200) / 15
        speed.y = (y + 200) / 15

#Función para determinar si un objeto se encuentra en pantalla o no, usado tanto proyectil como objetvos
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Dibuja los proyectiles y el proyectil en pantalla conforme a la información generada en las otras funciones
def draw():

    clear()

    #Dibuja los objetivos de azul
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    #Dibuja el proyectil de rojo
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#Función de movimiento para los objetivos y proyectil
def move():
    #Cambiamos el lugar de definición de la coordenada y para que se tome en cuenta como general
    y = randrange(-150, 150)
    #Se genera un nuevo objetivo cada cierto tiempo
    if randrange(40) == 0:
        #Primero se genera en la coordenada y generada arriba de manera aleatoria y en el x fuera de la pantalla
        target = vector(200, y)
        targets.append(target)

    #Se mueve el objetivo un poco a la izquierda con cada refresh
    for target in targets:
        target.x -= 0.5

    #Se implementa la gravedad en el proyectil
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    #Si se alcanza un objetivo con el proyectil, se elimina el objetivo de la lista de objetivos y desaparece de pantalla
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        #En esta parte, es donde se detenía el juego con 'return', pero ahora, vuelve a tomar las coordenadas orginales del objetivo para reiniciarlo
        if not inside(target):
            target = vector(200,y)

    ontimer(move, 30)

#Genera la pantalla gráfica
setup(420, 420, 370, 0)
#Oculta la tortuga que genera los dibujos
hideturtle()
up()
#Evita que la pantalla se dibuje en repetidas ocaciones, pues esta acción se hace manualmente
tracer(False)
#Obtiene las coordenadas del clic y las manda a la funcióon para determinar la velocidad del proyectil
onscreenclick(tap)
#Movimiento de todo
move()
done()
