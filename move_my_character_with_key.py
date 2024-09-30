from pico2d import *

open_canvas()
tuk = load_image('TUK_GROUND.png')
character = load_image('sonic_sheet.png')

def handle_events():
    global running, dir_x, dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

running = True
x = 240
y = 140
dir_x = 0
dir_y = 0
run = [140, 150, 145, 155]
run_bottom = [610, 750, 900, 1045]
i = 0

while running:
    clear_canvas()
    tuk.draw_to_origin(0, 0, 800, 600)
    character.clip_draw(run_bottom[i], 170, run[i], 190, x, y, 70, 70)
    i = (i + 1) % 4
    update_canvas()
    handle_events()
    x += dir_x * 10
    y += dir_y * 10


    if x < 35:
        x = 35
    elif x > 800 - 35:
        x = 800 - 35

    if y < 35:
        y = 35
    elif y > 600 - 35:
        y = 600 - 35

    delay(0.05)

close_canvas()

#뛰는 소닉
#850 660
#170 ~ 360 h
#610 ~ 750 / 750 ~ 900 / 900 ~ 1045 / 1045 ~ 1200 w
#구르는 소닉
#1020 860
#0 ~ 160 h
#0~160 / 160 ~ 290 / 290 ~ 430 / 430 ~ 565 / 565 ~ 710 w