from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
SCREEN_WIDTH1 = 640
SCREEN_HEIGHT = 480
black = Color(0, 1)
speed = 2.5
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)


thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
cf = PolygonAsset(((-10,-15),(10,-15),(10,15),(-10,15)), thinline, gray)
class MC(Sprite):
    def __init__(self, position):
        super().__init__(cf, position)
        
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, white)
        bg = Sprite(bg_asset, (0,0))
        
       
            


myapp = SpaceGame(SCREEN_WIDTH1, SCREEN_HEIGHT)

turn = 0
def turnProgress (event):
    global turn = 1
def spaceKey (event):
    turnProgress()
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)



myapp.run()