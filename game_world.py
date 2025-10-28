from pico2d import *
#world[0] 가장 낮은 계층 layer
#world[1] 그 다음 계층 layer
world = [[],[]]


def add_object(o, depth=0):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print("삭제하려는 오브젝트가 월드에 없습니다.")
def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    clear_canvas()
    for layer in world:
        for o in layer:
            o.draw()
    update_canvas()