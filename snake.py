from tkinter import font
import turtle #
import time 
import random
import pygame

def snake():
    from tkinter import font
    import turtle #
    import time 
    import random
    import pygame

    posponer = 0.1

    #Marrcador
    score = 0 
    score = 0 
    high_score = 0 

    #Configuración de la ventana 
    wn = turtle.Screen()
    wn.title("Juego de Snake")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)

    #Cabeza de la serpiente 
    cabeza = turtle.Turtle() #Creación del objeto
    cabeza.speed(0)
    cabeza.shape("square") #Para que tenga forma de cuadrado 
    cabeza.color("white")
    cabeza.penup() #No deja ningun rastro 
    cabeza.goto(0,0)
    cabeza.direction = "stop" #Apenas inicie el juego este en stop

    #Objeto COmida
    comida = turtle.Turtle() #Creación del objeto
    comida.speed(0)
    comida.shape("circle") #Para que tenga forma de circulo 
    comida.color("red")
    comida.penup() #No deja ningun rastro 
    cabeza.goto(0,100)


    #Cuerpo de la serpiente a traves de una lista
    segmentos = []


    #Marcador
    texto = turtle.Turtle()
    texto.speed(0) #Para que apenas abramos la pantalla el texto aparezca de una ve
    texto.color("white")
    texto.penup()
    texto.hideturtle()
    texto.goto(0,260)
    texto.write("Score: 0         High Score: 0", align="center", font=("Courier", 24, "normal"))


    ##Funcion de teclado
    def arriba():
        cabeza.direction = "up"

    def abajo():
        cabeza.direction = "down"

    def derecha():
        cabeza.direction = "right"

    def izquierda():
        cabeza.direction = "left"


    #Funcione de movimiento
    def mov():
        if cabeza.direction == "up":
            y = cabeza.ycor() #Guarda la coordenada actual de la cabeza en una variable
            cabeza.sety(y + 20)
            
        if cabeza.direction == "down":
            y = cabeza.ycor() #Guarda la coordenada actual de la cabeza en una variable
            cabeza.sety(y - 20)

        if cabeza.direction == "left":
            x = cabeza.xcor() #Guarda la coordenada actual de la cabeza en una variable
            cabeza.setx(x - 20)
            
        if cabeza.direction == "right":
            x = cabeza.xcor() #Guarda la coordenada actual de la cabeza en una variable
            cabeza.setx(x + 20)

    #Teclado
    wn.listen()
    wn.onkeypress(arriba, "Up")
    wn.onkeypress(abajo, "Down")
    wn.onkeypress(derecha, "Right")
    wn.onkeypress(izquierda, "Left")

    #Buqle Principal Obligatorio
    while True:
        wn.update()

        #Serpiente Muere si toca el limite del cuadro
        if cabeza.xcor()>280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
            time.sleep(1) #se pausa un momento el juego
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Vamos a esconder los segmentos
            for segmento in segmentos: 
                segmento.goto(2000,2000)
            
            segmentos.clear()
            


        #Cambiaremos la posicion de la comida una vez la haya tocado
        if cabeza.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x,y)

            nuevo_segmento = turtle.Turtle() #Creación del objeto
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square") #Para que tenga forma de cuadrado 
            nuevo_segmento.color("grey")
            nuevo_segmento.penup() #No deja ningun rastro 
            nuevo_segmento.goto(0,0)
            segmentos.append(nuevo_segmento) #agregamos a lista 

            #Aumentar Marcador
            score += 10

            if score > high_score:
                high_score = score
            
            texto.clear()
            texto.write("Score: {}         High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

        #Mover el cuerpo de la serpiente
        totalSeg = len(segmentos) #obtenemos el total de los segmentos que tenemos
        for index in range(totalSeg -1, 0, -1):
            x = segmentos[index - 1].xcor()
            y = segmentos [index - 1].ycor()
            segmentos[index].goto(x,y)

        if totalSeg > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            segmentos [0].goto(x,y)


        mov()
        time.sleep(posponer) #Para que el programa no se ejecute o se cierre tan rapido
    