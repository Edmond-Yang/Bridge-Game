import pygame as pg, random
from ..Objects import Road, Background, Label, Button

class Game_process :

    def __init__(self, game, info) :

        # game main
        self.game = game

        # game body(Game_trial)
        self.info = info

        # initialize data
        # Background
        self.num_bg = 0
        self.image_bg = {}
        for num in range(1,4) :
            self.image_bg[num] = Background.Background(self.game.screen, num)
        self.Bg()

        # Score
        self.score = 0
        self.font = pg.font.SysFont("Calibri", 20)
        self.txt_score = self.font.render("Score {:>5s}".format(str(self.score*100)), True, (0,0,0))

        # End Score
        self.fnt = pg.font.SysFont("Calibri", 35, True)
        self.txt_end = self.fnt.render("Score {:>5s}".format(str(self.score*100)), True, (255,255,255))

        # Perfect
        font = pg.font.SysFont("Calibri", 40)
        self.txt_perfect = font.render("Perfect", True, (43,94,0))
        self.state_perfect = False

        # Difficulty
        self.prob = []
        self.Difficulty()

        # Label
        self.label_restart = Label.Label(self.game.screen, "end", 0, 200)

        # Restart
        self.state_restart = False
        self.button_restart = Button.Button(self.game.screen, "restart", 20, 300)

        # Exit
        self.button_exit = Button.Button(self.game.screen, "exit", 250, 300)


    def Bg(self) :

        # initialize background
        if self.num_bg == 0 :
            
            self.num_bg += 1
            self.image_bg[self.num_bg].move(-1 * self.game.screen.get_width())

            return

        # another background will be show if the background  is disappearing
        if self.image_bg[self.num_bg].get_Left() <= -1 * self.image_bg[self.num_bg].get_Width() :

            self.image_bg[self.num_bg].reset()
            self.num_bg = self.num_bg + 1 if self.num_bg < 3 else 1

        # if length is assigned or not
        
        self.image_bg[self.num_bg].move()
        self.image_bg[self.num_bg + 1].move() if  self.num_bg < 3 else  self.image_bg[1].move()


    def Road_mode_easy(self) :
        
        # initialize road 
        if len(self.info.road) == 0 :

            self.info.road.append( Road.Road(self.game.screen, self.prob, 1, -35 ) )

            while self.info.road[-1].get_Left() <= self.game.screen.get_width() :
                
                length_gap = random.randint(30, 150) 
                self.info.road.append( Road.Road(screen = self.game.screen, table_prob = self.prob, x = self.info.road[-1].get_Right() + length_gap ) )

        # if the last road appeared, the new road and gap will be created
        if self.info.road[-1].get_Left() <= self.game.screen.get_width() :

            length_gap = random.randint(30, 150) 
            self.info.road.append( Road.Road(screen = self.game.screen, table_prob = self.prob, x = self.info.road[-1].get_Right() + length_gap ) )


    def Road_mode_hard(self) :

        if len(self.info.road) == 0:
            self.info.road.append( Road.Road(self.game.screen, self.prob, 1, -35 ) )
            length_gap = random.randint(60, 150) 
            self.info.road.append( Road.Road(screen = self.game.screen, table_prob = self.prob, x = self.info.road[-1].get_Right() + length_gap ) )

        elif len(self.info.road) == 1:
            length_gap = random.randint(60, 150)
            self.info.road.append( Road.Road(screen = self.game.screen, table_prob = self.prob, x = self.info.road[-1].get_Right() + length_gap ) )
        
        self.info.road[1].Keep_Moving(self.info.num_bridge)


    def Thrown(self) :

        # throw useless road and gap
        for i in range(0, self.info.num_bridge) :
            self.info.road.pop(0)


    def Score(self, score = 1) :

        # calculate score and change score on window

        self.score += score
        self.txt_score = self.font.render("Score {:>5s}".format(str(self.score*100)), True, (0,0,0))


    def Difficulty(self) :
    
        # change the probability with score

        if self.score < 5 :
            self.prob = [0.80, 0.10, 0.10, 0, 0, 0, 0, 0]

        elif self.score < 10 :
            self.prob = [0.60, 0.25, 0.15,  0, 0, 0, 0, 0]

        elif self.score < 15 :
            self.prob = [0.5, 0.3, 0.15, 0.05, 0, 0, 0, 0]

        elif self.score < 20 :
            self.prob = [0.30, 0.30, 0.15, 0.15, 0.05, 0.05, 0, 0]

        elif self.score < 25 :
            self.prob = [0.20, 0.20, 0.15, 0.15, 0.10, 0.10, 0.10, 0]

        else :
            self.prob = [0.15, 0.15, 0.15, 0.15, 0.10, 0.10, 0.10, 0.10]


    def restart(self, mouse, position) :
        
        # person is not completely falling
        if not self.state_restart :
            return False, False

        # blit anything
        self.blit()

        self.label_restart.blit()
        self.button_restart.blit()
        self.button_exit.blit()

        self.txt_end = self.fnt.render("Score {:>5s}".format( str(self.score*100) ), True, (255,255,255))
        self.game.screen.blit( self.txt_end , (100,250) )
        
        # detect if press the button or not
        if self.button_restart.detect_press(mouse, position) :
            return True, True
            
        if self.button_exit.detect_press(mouse, position) :
            self.game.running = False
        
        # return "falling" and "restart" means if the motion is completed
        return True, False


    def blit(self) :
    
        # painter
        self.game.screen.blit( self.game.painter , (0,0) )

        # background
        self.image_bg[self.num_bg].blit()
        self.image_bg[self.num_bg + 1].blit() if self.num_bg < 3 else self.image_bg[1].blit()

        # road
        for road in self.info.road :
            road.blit()

        # person
        self.state_restart = self.info.person.blit()

        # score
        self.game.screen.blit( self.txt_score, (240, 30) )

        # Perfect
        if self.state_perfect :
            self.game.screen.blit( self.txt_perfect, (120,100) )
