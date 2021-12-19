import pygame

from pygame import Vector2
from pygame.threads import STOP
from Settings import*
from Bird import Bird 

def rule1(bird, flock):
    """
    Separate this bird from other birds if they are too close
    
    param: bird - current exemplar of class Bird
    param: flock - other elements of class Bird

    return: None
    
    """
    Power_of_ATTRACTION = ATTRACTION * (RADIUS - (bird.get_pos().distance_to(flock.get_pos()))) / RADIUS
    Force = (bird.get_vel() - flock.get_vel()).normalize()
    Force.scale_to_length(Power_of_ATTRACTION)
    bird.push(Force)

def rule2(bird, flock):
    """
    Direct this bird in the same direction with other birds
    
    param: bird - current exemplar of class Bird
    param: flock - other elements of class Bird

    return: None
    
    """
    Power_of_ATTRACTION = 10 * ATTRACTION * (RADIUS - (bird.get_pos().distance_to(flock.get_pos()))) / RADIUS
    Force = flock.get_vel().normalize()
    Force.scale_to_length(Power_of_ATTRACTION)
    bird.push(Force)

def rule3(bird, flock):
    """
    Gather birds together if they are too far from each other
        
    param: bird - current exemplar of class Bird
    param: flock - other elements of class Bird

    return: None
    
    """
    Power_of_ATTRACTION = ATTRACTION * bird.get_pos().distance_to(flock.get_pos()) / RADIUS
    Force = (flock.get_vel() - bird.get_vel()).normalize()
    Force.scale_to_length(Power_of_ATTRACTION)
    bird.push(Force)

def detect(bird, flock):
    """
    Find other birds within th efield of view of this bird
           
    param: bird - current exemplar of class Bird
    param: flock - other elements of class Bird

    return: True if this bird see other birds
            False if this bird can not see other birds
    
    """
    distance = bird.get_pos().distance_to(flock.get_pos())
    if distance < VIEW_DISTANCE: 
         return True
    else:
        return False

def behavior(bird):
    """
    Apply rules for each bird
    
    param: bird - current exemplar of class Bird

    return: None

    """
    for flock in birds:
        if flock is not bird:
            if detect(bird, flock):
                rule1(bird, flock)
                rule2(bird, flock)
                rule3(bird, flock)

def draw_bird(bird):
    """
    Draw birds

    param: bird - current exemplar of class Bird

    return: None

    """
    top = bird.get_pos()/1.2 + Vector2(WIDTH//8, HEIGHT//8) - Vector2(pygame.mouse.get_pos())/5
    vert1 = top - bird.get_vel().rotate(-15) * 3
    vert2 = top - bird.get_vel().rotate(15) * 3
    pygame.draw.polygon(screen, bird.get_color(), [top , vert1, vert2]) 

screen = pygame.display.set_mode([WIDTH, HEIGHT]) #New screen
birds = [Bird() for _ in range(BIRD_NUM)]         #New array of bird

def run():
    """
    Run whole application

    param: None

    return: None
    
    """
    STOP = False
    while not STOP:
        screen.fill((50, 50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                STOP = True

        for bird in birds:
            behavior(bird)
            bird.move()
            draw_bird(bird)
        
        pygame.display.update()
        

if __name__ == '__main__' :
    run()