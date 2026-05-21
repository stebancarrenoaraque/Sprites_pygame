import pygame  # Librería principal para el juego 
import sys     # Para cerrar la aplicación por completo 

# Definición de colores
COLOR_ROJO = (255, 0, 0)
COLOR_AZUL = (0, 0, 255)

# 1. CLASE DEL SPRITE 
class CUADRADO(pygame.sprite.Sprite):  # Hereda de la clase Sprite de Pygame
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Inicializa la clase madre
        
        # Dimensiones y color del cuadrado
        self.image = pygame.Surface((80, 80))
        self.image.fill(COLOR_ROJO)
        
        # Rectángulo para controlar posición física
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        
        # Píxeles que se moverá por cada fotograma
        self.DESPLAZAMIENTO = 3

    def update(self):  # Método automático de actualización 
        self.rect.x += self.DESPLAZAMIENTO  # Mueve el cuadrado en el eje X
        
        # Rebotar si toca el borde derecho 
        if self.rect.x >= 320:
            self.rect.x = 320
            self.DESPLAZAMIENTO = -3  # Cambia dirección a la izquierda
            
        # Rebotar si toca el borde izquierdo
        elif self.rect.x <= 0:
            self.rect.x = 0
            self.DESPLAZAMIENTO = 3   # Cambia dirección a la derecha

# 2. CONFIGURACIÓN DEL ENTORNO
pygame.init()  # Inicializa Pygame
screen = pygame.display.set_mode((400, 400))  # Ventana de 400x400
pygame.display.set_caption("El cuadrado que rebota")  # Título de la ventana

# Crear y dibujar el fondo azul
background = pygame.Surface(screen.get_size())
background.fill(COLOR_AZUL)
screen.blit(background, (0, 0))

reloj = pygame.time.Clock()  # Reloj para controlar los FPS 

# Creación del grupo y de la instancia del sprite 
all_sprites = pygame.sprite.Group()  # Contenedor de sprites
cuadrado = CUADRADO()                # Creamos el objeto cuadrado
all_sprites.add(cuadrado)            # Lo añadimos al grupo

# 3. BUCLE PRINCIPAL
while True:
    # Captura eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detecta si se cierra la ventana
            pygame.quit()
            sys.exit()                 # Cierra el programa
            
    # Ciclo de renderizado: Limpiar -> Actualizar -> Dibujar
    all_sprites.clear(screen, background)  # Borra la posición anterior
    all_sprites.update()                  # Calcula la nueva posición
    all_sprites.draw(screen)              # Dibuja en la nueva posición
    
    pygame.display.flip()  # Actualiza los gráficos en pantalla
    reloj.tick(60)         # Corre el juego a 60 fotogramas por segundo