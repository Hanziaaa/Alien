import pgzrun,random  
#
WIDTH=500
HEIGHT=500
TITLE="Alien Shoot"
#
alien=Actor("aliengame")
message=""

def placealien():
    alien.x=random.randint(50,WIDTH-50)
    alien.y=random.randint(50,WIDTH-50)
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message = "Good Shot!"
        placealien()
    else: 
        message="You missed!"    
        placealien()



def draw():
    screen.clear()
    screen.fill(color=(125,0,0))
    alien.draw()
    screen.draw.text(message, center = (250,10), fontsize=30,color= "blue")



pgzrun.go()