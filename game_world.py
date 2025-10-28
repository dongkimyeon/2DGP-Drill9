from pico2d import *
world = []


def add_object(o):
    world.append(o)

def remove_object(o):
    if o in world:
        world.remove(o)
    else:
        print("삭제하려는 오브젝트가 월드에 없습니다.")
def update():
    for o in world:
        o.update()

def render():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()