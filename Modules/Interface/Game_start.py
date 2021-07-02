from PIL import Image
from . import Game_process, Game_trial
from ..Objects import Button, Label, Person, Color

class Game_Start :

    def __init__(self, game) :

        # initialize anything

        self.game = game
        self.processor = Game_process.Game_process(game, self)

        self.state = False
        self.start = False

        self.label_start = Label.Label(self.game.screen, "start", 0, 200)
        self.button_start = Button.Button(self.game.screen, "start", 20, 300)
        self.button_Go = Button.Button(self.game.screen, "go", 130, 310)

        self.state_color = False
        self.label_color = Color.Color(self.game.screen,"color", 30, 375)
        self.button_color = Button.Button(self.game.screen, "color", 250, 300)

        self.set_color(self.game.current_color)

        self.person = Person.Person(self.game.screen)
        self.person.set_Status("Running")
        self.person.set_Position(175, 175)

        self.label_mode = Label.Label(self.game.screen, "mode", 0, 200)
        self.button_arrow_right = Button.Button(self.game.screen, "arrow_right", 300, 255)
        self.button_arrow_left = Button.Button(self.game.screen, "arrow_left", 30, 255)

        self.state_mode = False
        self.mode = ["Easy", "Medium", "Hard"]
        self.txt_mode = self.processor.fnt.render( self.mode[self.game.num_mode], True, (255,255,255) ) 

    
    def begin(self, mouse, position) :

        if self.state :
            return True

        self.processor.Bg()
        
        if self.start :
            self.state = self.set_Mode(mouse, position)
            return False
        
        self.blit()

        if self.state_color :

            self.label_color.blit()

            state, color = self.label_color.detect_press(mouse, position)

            if self.button_color.detect_press(mouse, position) :
                self.state_color = False
            
            if state :
                self.set_color(color)
                self.person = Person.Person(self.game.screen)
                self.person.set_Status("Running")
                self.person.set_Position(175, 175)

        else :

            if self.button_color.detect_press(mouse, position) :
                self.state_color = True

            if self.button_start.detect_press(mouse, position) :
                self.start = True
        
        return self.state


    def set_Mode(self, mouse, position) :

        self.blit_mode()

        if self.button_arrow_right.detect_press(mouse, position) :
            self.game.num_mode = self.game.num_mode + 1 if self.game.num_mode < 2 else 0

        if self.button_arrow_left.detect_press(mouse, position) :
            self.game.num_mode = self.game.num_mode - 1 if self.game.num_mode > 0 else 2
        
        if self.button_Go.detect_press(mouse, position) :
            self.game.game = Game_trial.Game_trial(self.game)
            self.game.sound_Gaming() 
            return True

        return False
        

    def set_color(self, color = (0,0,0,255) ) :
        
        self.game.current_color = color

        for i in range(1,9) :

            address_img = "icon_" + str(i)

            image = Image.open("./Photo/" + address_img + ".png")
            image = image.convert("RGBA")

            if color == (0,0,0,255) :
                image.save("./Photo/new_" + address_img + ".png", "PNG")
                continue

            else :
                data = image.getdata()
                new_data = []

            for item in data :

                if item[3] == 0 or ( item[0] != 0 or item[1] != 0 or item[2] != 0 ) :
                    new_data.append( item )
                else :
                    new_data.append( color )

            image.putdata(new_data)
            image.save("./Photo/new_" + address_img + ".png", "PNG") 


    def blit(self) :

        # painter
        self.game.screen.blit( self.game.painter , (0,0) )

        # background
        self.processor.image_bg[self.processor.num_bg].blit()
        self.processor.image_bg[self.processor.num_bg + 1].blit() if self.processor.num_bg < 3 else self.processor.image_bg[1].blit()

        # label
        self.label_start.blit()

        # person
        self.person.blit()

        # button
        self.button_color.blit()
        self.button_start.blit()

    def blit_mode(self) :

        # painter
        self.game.screen.blit( self.game.painter , (0,0) )

        # background
        self.processor.image_bg[self.processor.num_bg].blit()
        self.processor.image_bg[self.processor.num_bg + 1].blit() if self.processor.num_bg < 3 else self.processor.image_bg[1].blit()

        # label
        self.label_mode.blit()

        # person
        self.person.set_Position(170, 140)
        self.person.blit()

        # txt
        self.txt_mode = self.processor.fnt.render( self.mode[self.game.num_mode], True, (255,255,255) )
        self.game.screen.blit( self.txt_mode, (118, 255) ) if self.game.num_mode == 1 else self.game.screen.blit( self.txt_mode, (146, 255) )

        # button
        self.button_arrow_left.blit()
        self.button_arrow_right.blit()
        self.button_Go.blit()
