from Modules.Interface import Game_start
import pygame as pg

class Bridge_game :

    def __init__(self) :

        # initialize pygame
        pg.init()

        # for update times
        self.clock = pg.time.Clock()

        # create an window
        width, height = 360, 600
        pg.display.set_caption("Bridge Game")
        self.screen = pg.display.set_mode( (width, height) )

        # set icon
        icon = pg.image.load("./Photo/icon_1.png")
        icon.convert()
        pg.display.set_icon(icon)
        
        # create a painter(Surface)
        self.painter = pg.Surface( self.screen.get_size() )
        self.painter = self.painter.convert()
        self.painter.fill( (219, 239, 238) )

        # import game body
        self.num_mode = 0
        self.current_color = (0, 0, 0, 255)
        self.start = Game_start.Game_Start(self)

        # initialize music
        pg.mixer.init()

        # background music channel
        self.background_music = pg.mixer.Channel(1)
        self.sound_Entering()

        # falling effect channel
        self.effect = pg.mixer.Channel(2)

        # for game loop
        self.run_Coding()

    
    def sound_Entering(self) :
        self.background_music.play( pg.mixer.Sound("./Music/Main Theme.wav"), -1)
        self.background_music.set_volume(0.2)

    def sound_Gaming(self) :
        self.background_music.play( pg.mixer.Sound("./Music/Background Music_" + str(self.num_mode) +".wav"), -1)
        self.background_music.set_volume(0.3) if self.num_mode == 0 else  self.background_music.set_volume(0.2)

    def sound_Falling(self) :
        
        # pause background music(volume = 0) and play falling effect 
        self.background_music.set_volume(0)
        self.effect.play( pg.mixer.Sound("./Music/Falling Effect.wav") )
        self.effect.set_volume(0.1)

    def sound_Perfect(self) :
        
        # pause background music(volume = 0) and play falling effect 
        self.effect.play( pg.mixer.Sound("./Music/Perfect Effect.wav") )
        self.effect.set_volume(0.1)

       
    def run_Coding(self) :

        self.running = True

        while self.running :
            
            # update times per second
            self.clock.tick(60)

            # exit or not
            for event in pg.event.get() :
                if event.type == pg.QUIT :
                    self.running = False

            # click mouse or not
            mouse = pg.mouse.get_pressed()
            position = pg.mouse.get_pos()
            
            # execute game body
            if( self.start.begin(mouse, position) ) :

                if self.game.trial(mouse, position) :
                    self.start = Game_start.Game_Start(self)
                    self.sound_Entering()
            
            # update 
            pg.display.update()

        pg.quit()

if __name__ == "__main__" :
    Bridge_game()