import pyxel
from Frame import Frame

class App:
    def __init__(self):
        width = int(1920/2)
        height = int(1080 /2)
        pyxel.init(width, height,  title="色戦争げーむ")

        frame_w =  frame_h = height
        frame_x = int((width - frame_w) / 2 )
        frame_y = int((height - frame_h) / 2)
        frame_c = 7
        self.frame = Frame(frame_x, frame_y, frame_w, frame_h, frame_c)
    
    def run(self):
        pyxel.run(self.update, self.draw)
        


    
    def update(self):
        self.frame.update()
        pass

    def draw(self):
        pyxel.cls(7)
        self.frame.draw()
        # pyxel.text(55, 41, "Hello, World!", 7)

if __name__ == '__main__':
    app = App()
    app.run()

