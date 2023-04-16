import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
circles = []
line_points = []

# LINE VARIABLES
line_colors = (255, 255, 255)
line_width = 25

starting_pos = (750, 250)
ending_pos = (800, 250)

circles.append({"pos": starting_pos, "color": (0, 255, 0)})
circles.append({"pos": ending_pos, "color": (255, 0, 0)})

line_drawn = False
line_finished = False
raceTrackFinished = False

while running:
    mouse_pos = pygame.mouse.get_pos()

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d:
                line_points = circles
                circles = []
                line_drawn = True
            if event.key == pygame.K_s:
                pygame.image.save(screen, "track.png")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0, 0, 0))

    # DRAW YOUR GAME HERE
    if raceTrackFinished is False:
        if line_drawn is False:
            if pygame.mouse.get_pressed()[0]:
                if starting_pos:
                    circles.append({"pos": mouse_pos, "color": (0, 0, 255)})
                starting_pos = mouse_pos

                # Check if the line is finished
                if abs(mouse_pos[0] - ending_pos[0]) <= 10 and abs(mouse_pos[1] - ending_pos[1]) <= 10:
                    line_finished = True

            # RENDER YOUR GAME HERE
            for circle in circles:
                pygame.draw.circle(screen, circle["color"], circle["pos"], 10)

            if len(circles) > 1:
                circle_pos = []

                for circle in circles:
                    circle_pos.append(circle["pos"])

                pygame.draw.lines(screen, line_colors, False, circle_pos, line_width)

        else:
            pygame.draw.lines(screen, line_colors, False, line_points, line_width)
            pygame.draw.circle(screen, (255, 0, 0), starting_pos, 10)
            pygame.draw.circle(screen, (255, 0, 0), line_points[-1], 10)

            # Check if the line is finished
            if abs(mouse_pos[0] - ending_pos[0]) <= 10 and abs(mouse_pos[1] - ending_pos[1]) <= 10:
                line_finished = True

        # flip() the display to put your work on screen
        # limits FPS to 60

        # Stop drawing if the line is finished
        if line_finished:
            raceTrackFinished = True

            for circle in circles:
                # save all pos to a list
                line_points.append(circle["pos"])

            circles = []
    else:
        # export the line_points to an image
        pygame.draw.lines(screen, line_colors, False, line_points, line_width)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
