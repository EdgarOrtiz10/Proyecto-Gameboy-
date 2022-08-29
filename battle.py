import pygame, random, math
from pygame import mixer #mixer es para los sonidos
from pynput import keyboard as kb

def battle():
    screen = pygame.display.set_mode((800, 600)) # crea la pantalla, en este caso de 800px * 600px
    background = pygame.image.load('./assets/img/fondo.png')
    mixer.music.load("./assets/img/sound.mp3")
    mixer.music.play(-1) #loop de la musica o sonido

    pygame.display.set_caption("Empire Tanks") #titulo de la ventana 
    icon = pygame.image.load('./assets/img/icon.png') 
    pygame.display.set_icon(icon) #icono de la ventana

    playerImg = pygame.image.load('./assets/img/tanque.png') #player imagen
    playerX = 370 #player posicion
    playerY = 480
    playerX_change = 0 #player variable de movimiento en x

    #enemyImg = pygame.image.load('enemigo.png') #enemigo imagen
    #enemyX = random.randint(0, 736) #enemigo posicion
    #enemyY = random.randint(50, 150)
    #enemyX_change = 0 #enemigo variable movimiento en x
    #enemyY_change = 0

    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 10

    bulletImg = pygame.image.load('./assets/img/bullet.png') #imagen del disparo
    bulletX = 0 #posicion inicial
    bulletY = 480
    bulletX_change = 0 #variables de movimiento
    bulletY_change = 20
    bullet_state = "ready" #variable de estado

    score_value = 0 #variable para hacer el conteo de enemigos muertos
    font = pygame.font.Font('freesansbold.ttf', 32) # el numero es el tamaño de la fuente
    textX = 10 #posicion inicial
    testY = 10

    over_font = pygame.font.Font('freesansbold.ttf', 64)


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (0, 255, 0)) # concatenamos una string con la variable score(enemigos muertos), pero primero convertimos esta variable a string
        screen.blit(score, (x, y))


    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (0, 255, 0))
        screen.blit(over_text, (200, 250))


    def player(x, y):
        screen.blit(playerImg, (x, y))


    #def enemy(x, y,):
        #screen.blit(enemyImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyImg[i], (x, y))


    def fire_bullet(x, y):
        global bullet_state #la definimos como global, pues la vamos a utilizar fuera de este metodo
        bullet_state = "fire" # si recordamos esta variable es inicializada como "ready" al invocar este metodo dentro del juego o mejor al disparar su estado pasa a "fire"
        screen.blit(bulletImg, (x + 16, y + 10)) # se le suma estos valores para centrarlos al personaje


    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
        #al determinar esta distancia entre objetos se puede saber que tan cerca estan el uno del otro
        if distance < 27:
            return True
        else:
            return False

        
    #----- Cargamos las imagenes de la explosion ----------
    explosion_anim = []
    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('./assets/img/enemigo.png'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(2)
        enemyY_change.append(40)
        
    #class Explosion(pygame.sprite.Sprite):
    #    def __init___(self, center):  #Centrar la explosion en el centro del punto
    #        super().__init__()
    #        self.image = explosion_anim[0]
    #        self.rect = self.image.get_rect()
    #        self.rect.center = center
    #        self.frame = 0
    #        self.last_update = pygame.time.get_ticks()
    #        self.frame_rate = 50 #Velocidad de la explosión
            
    #    def update(self):
    #        now = pygame.time.get_ticks() #Cuanto tiempo ha transcurrido 
    #        if now - self.last_update > self.frame_rate:
    #            self.last_update = now
    #            self.frame += 1 #Incrementa la variable para pasar por todos los elementos de la lista
    #            if self.frame == len(explosion_anim):
    #                self.kill()
    #            else:
    #                center = self.rect.center
    #                self.image = explosion_anim[self.frame]
    #                self.rect = self.image.get_rect()
    #                self.rect.center = center
                


    running = True #variable boleana para detener el loop del juego, se declara en true.
    while running: #este es el loop del juego, recordar que esta es la base de todo juego un constante loop.

        screen.fill((0, 0, 0)) # RGB = (Red, Green, Blue) esta  linea determnia el color de la pantalla, en este caso es negra por su color en RGB.
        screen.blit(background, (0, 0))
        for event in pygame.event.get(): #estamos invocando los eventos que ocurran mientras este corriendo el loop (while)
            if event.type == pygame.QUIT: #esta condicion nos permite salir del juego o terminarlo
                running = False #y al declarar la variable running false el while se detiene 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerImg = pygame.transform.rotate(playerImg, 90)
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerImg = pygame.transform.rotate(playerImg, -90)
                    playerX_change = 5
                
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletSound = mixer.Sound("./assets/img/disparo.mp3")
                        bulletSound.play()
                        # igualamos la posicion del disparo con el player, esto para dar la sensacion de que sale del player el disparo
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerImg = pygame.transform.rotate(playerImg, -90)
                    playerX_change = 0    #aqui, le damos este valor a la variable para player se quede quieto en su posicion actual 
                if event.key == pygame.K_RIGHT:
                    playerImg = pygame.transform.rotate(playerImg, 90)
                    playerX_change = 0


        playerX += playerX_change #esto da el movimiento al player
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        #Lugar for Enemy

        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over-> se determina que el juego termina cuando los enemigos superan la linea de los 440 pixeles
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break
            #este es el movimiento de lado a lado y al tocar los limites baja un renglon y se devuelven de lado a lado
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]

            # Collision -> si collision es TRUE se activa el sonido de explosion / la posicion de la bala es 480 pixeles / la bala tiene estado: ready / la variable score aumenta uno
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                #explosion = Explosion()
                explosionSound = mixer.Sound("./assets/img/explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                # el enemigo se regenera o inicializa en otra posicion aleatoriamente
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0: #movimiento al disparo
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change #esto es para crear un nuevo disparo en la posicion inicial y
            bulletX -= bulletX_change


        #enemy(enemyX, enemyY) # metodo enemigo *** borrar al colocar nuevo for enemy
        player(playerX, playerY) #metodo player
        show_score(textX, testY) #metodo para el score
        pygame.display.flip() #Actualizar pantalla
        pygame.display.update() #actualiza el juego 
