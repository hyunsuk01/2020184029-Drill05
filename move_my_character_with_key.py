from pico2d import *

open_canvas()
tuk = load_image('TUK_GROUND.png')
character = load_image('sonic_sheet.png')

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            pass
        elif event.type == SDL_KEYUP:
            pass

running = True

while running:
    clear_canvas()
    tuk.draw_to_origin(0, 0, 800, 600)
    update_canvas()
    handle_events()

    delay(0.05)

close_canvas()