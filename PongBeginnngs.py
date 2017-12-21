import pygame,sys,time

# By Kyle Yen - Period 4

BLACK = (0,0,0)
WHITE = (255,255,255)

def main():
    pygame.init()

    width = 920
    height = 570

    # Dimensions and speed of ball
    ball_width = ball_height = 20
    ball_speed = [5, 5]

    # Dimensions and speed of paddles
    p_width = 20
    p_height = 70
    p_speed = 5

    # Settings for left paddle
    pl_x = width / 20
    pl_y = height/2 - p_height/2
    pl_move = 0

    # Settings for right paddle
    pr_x = width * 19 / 20
    pr_y = height / 2 - p_height / 2
    pr_move = 0

    # Displaying screen
    pygame.display.set_caption("Pong")
    screen = pygame.display.set_mode((width,height))

    # Setting paddles and ball as Surfaces
    paddle_left = pygame.Surface((p_width, p_height)).convert()
    pl_rect = pygame.Rect(pl_x, pl_y, p_width, p_height)
    paddle_left.fill(WHITE)

    paddle_right = pygame.Surface((p_width, p_height)).convert()
    pr_rect = pygame.Rect(pr_x, pr_y, p_width, p_height)
    paddle_right.fill(WHITE)

    ball = pygame.Surface((ball_width, ball_height)).convert()
    ball_rect = pygame.Rect(width / 2, height / 2 - (ball_height/2), ball_width, ball_height)
    ball.fill(WHITE)

    screen.fill(BLACK)

    # Game loop
    running = True
    while running:

        # Checks for valid player inputs during the game loop
        for event in pygame.event.get():
            # Allows the red button to function
            if event.type == pygame.QUIT:
                sys.exit()

            # Detects player inputs for the paddles
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pl_move = -1
                if event.key == pygame.K_s:
                    pl_move = 1

                if event.key == pygame.K_UP:
                    pr_move = -1
                if event.key == pygame.K_DOWN:
                    pr_move = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pl_move = 0
                if event.key == pygame.K_s:
                    pl_move = 0

                if event.key == pygame.K_UP:
                    pr_move = 0
                if event.key == pygame.K_DOWN:
                    pr_move = 0

        # Assigns new y-values for the paddles
        if pl_move != 0:
            pl_rect = pl_rect.move(0, pl_move * p_speed)
        if pr_move != 0:
            pr_rect = pr_rect.move(0, pr_move * p_speed)

        # Restricts paddles from going offscreen
        if pl_rect.top < 0:
            pl_rect.top = 0
        elif pl_rect.top > height - p_height:
            pl_rect.top = height - p_height
        if pr_rect.top < 0:
            pr_rect.top = 0
        elif pr_rect.top > height - p_height:
            pr_rect.top = height - p_height

        # Checks if ball runs into top/bottom walls
        if ball_rect.top > height - ball_rect.height or ball_rect.top < 0:
            ball_speed[1] = -ball_speed[1]

        # Moves ball
        ball_rect = ball_rect.move(ball_speed[0], ball_speed[1])

        # Checks if ball hits paddles
        # Hitting left paddle
        if pl_rect.right + 0.25 * abs(ball_speed[0]) > ball_rect.left > pl_rect.right - abs(ball_speed[0]) and pl_rect.bottom > ball_rect.top > pl_rect.top - ball_height:
            ball_speed[0] = abs(ball_speed[0])
        # Hitting right paddle
        elif pr_rect.left + abs(ball_speed[0]) > ball_rect.right > pr_rect.left - 0.25 * abs(ball_speed[0]) and pr_rect.bottom > ball_rect.top > pr_rect.top - ball_height:
            ball_speed[0] = -abs(ball_speed[0])

        # Removes trails from paddles/ball
        screen.fill(BLACK)

        # Displays the paddles and ball at their new positions
        screen.blit(paddle_left, pl_rect)
        screen.blit(paddle_right, pr_rect)
        screen.blit(ball, ball_rect)
        
        pygame.display.flip()

        if not width + ball_width > ball_rect.left > 0 - ball_width:
            print ball_rect.left
            time.sleep(1)
            running = False

if __name__ == "__main__":
    main()
