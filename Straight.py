from template import Controller

run = True
forward = False

while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.KRETURN]:
        if forward:
            Controller.stop()
            forward = False
        else:
            Controller.moveForward()
            forward = True
    elif keys[pygame.K_ESCAPE]:
        Controller.emergent()
    elif keys[pygame.K_s]:
        run = False
    time.sleep(1)

Controller.stop()
