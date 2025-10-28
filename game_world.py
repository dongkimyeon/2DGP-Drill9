from pico2d import *
world = []


def add_object(o):
    world.append(o)

def remove_object(o):
    world.remove(o)

def update():
    for o in world:
        o.update()

def render():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()