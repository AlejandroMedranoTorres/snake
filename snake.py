from turtle import *
from random import randrange
from freegames import square, vector
#importar las funciones square y vector del modulo free games
food = vector(0, 0)
color_num_food = randrange(0,5);
color_num_snake = randrange(0,5);
movimiento_comida = [vector(-10,0),vector(10,0),vector(0,-10),vector(0,10)]
snake = [vector(10, 0)]
aim = vector(0, -10)
colorlist = ["green","blue","yellow","cyan","purple"]
#definir las posiciones iniciales de la comida, la serpiente y el andonde va la serpiente

#cambiar la dirrección de la serpiente recibiendo los nuevos valores de "x" y "y"
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

#revisa que la cabeza de la serpienta este adentro
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

#función que se dedica a mover la serpiente
def move():
    
    
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
#revisa si la serpiente esta en contacto con la comida
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        global color_num_food
        global color_num_snake
        color_num_food = randrange(0,5);
        color_num_snake = randrange(0,5);
    else:
        snake.pop(0)
        food.move(movimiento_comida[randrange(0,4)])
        if not inside(food) or food in snake:
            square(food.x, food.y, 9, 'red')
            update()
            return

    clear()
#define las características del cuerpo de la serpiente 
    for body in snake:
        square(body.x, body.y, 9, colorlist[color_num_snake])

    square(food.x, food.y, 9, colorlist[color_num_food])
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#revisa las comandos y realiza una acción en base a esto
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
