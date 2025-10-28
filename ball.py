from pico2d import load_image
from game_world import remove_object
class Ball:
    image = None
    def __init__(self, x = 400,y = 300 ,velocity = 1):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        #화면 밖으로 나가면 객체 제거
        if self.x < 0 or self.x > 800:
            remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
