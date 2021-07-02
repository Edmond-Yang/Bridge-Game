from . import Game_process
from ..Objects import Bridge, Person 

class Game_trial :

    def __init__ (self, game) :
        
        # import main
        self.game = game

        # "import this" to process everything including moving background, creating road, deleting useless road etc
        self.process = Game_process.Game_process(game, self)

        # to initialize any variables 
        # Person
        self.person = Person.Person(self.game.screen)

        # Road
        self.road = []

        # Bridge
        self.bridge = Bridge.Bridge(self.game.screen, self.game.current_color)
        self.num_bridge = 0

        # to initialize difficulty
        self.process.Difficulty()

        # to create initial road
        self.process.Road_mode_easy() if self.game.num_mode == 0 else self.process.Road_mode_hard()
        

        
    def trial(self, mouse, position) :
        
        # to create road if it need

        if self.game.num_mode == 0 :
            self.process.Road_mode_easy()

        if self.game.num_mode == 2 and self.person.get_Status() not in ["Walking", "Running"]:
            self.process.Road_mode_hard()

        # to reset difficulty
        self.process.Difficulty()

        # check any status 
        # "Making" means making bridge
        if self.person.get_Status() == "Making" :
            self.making(mouse)

        # "Moving" means person cross through bridge
        elif self.person.get_Status() == "Moving" :
            self.moving()

        # "Walking" means person move back to his initial position
        elif self.person.get_Status() == "Walking" :
            self.walking()

        # "Running" means person move to road edge
        elif self.person.get_Status() == "Running" :
            self.running()

        # "Falling" means gamer lost the game (person didn't reach the road)
        elif self.person.get_Status() == "Falling" :
            
            falling, restart = self.process.restart(mouse, position)

            if restart :
                return  True
            if falling :
                return False  
        
        # prevent something wrong happens 
        else :
            print("Something Wrong with person status " + self.person.get_Status()  + "!")

        # blit anything(without line) in window
        self.process.blit()

        # blit line in window
        if self.person.get_Status() not in ["Walking","Running", "Falling"] :
            self.bridge.blit()

        return False


    def making(self, mouse) :

        # check bridge lengthen or not and rotated status 
        if self.bridge.detect_Press(mouse) :

            # change status to "Moving" as it is rotated
            self.person.set_Status("Moving")

        if self.game.num_mode == 1 :
            self.process.Road_mode_hard()


    def moving(self) :

        # person's postition should be at 5 + bridge's length (person's initial postition is 5 in x)
        if self.person.get_Left() == self.bridge.get_Length() + 5 :
            
            # check person is fallen or not (when "num_bridge" equals to 0, it means person couldn't stand on the road)
            self.falling()

            if self.num_bridge == 0 :
                self.person.set_Status("Falling")
            else :
                self.person.set_Status("Walking")

        # move slowly and prevent him to rush to another position
        else :
            self.person.move()


    def walking(self) :

        # person should move back to his initial position (at 5)
        if self.person.get_Left() == 5 :

            # change status
            self.person.set_Status("Running")

            # delete useless road and gap
            self.process.Thrown()

        else :
           
            # move background and prevent it to rush to another position
            self.process.Bg()
            
            # move person and prevent him to rush to another position
            self.person.move(-5)
            
            # move road and prevent it to rush to another position
            for road in self.road :
               road.move()
            

    def running(self) :

        # road must move forward to hit its initial position (at 30) or less
        if self.road[0].get_Right() <= 30 :

            # change Status
            self.process.state_perfect = False
            self.person.set_Status("Making")

            # reset the bridge
            self.bridge.reset()
        else :
            
            # move background
            self.process.Bg()
            
            # move road
            for road in self.road :
                road.move()


    def falling(self) :

        # judge which bridge he stands on (if no , I will let num equals to 0)

        length = self.bridge.get_Length() + 27

        for road in self.road :

            if length >= road.get_Left() -5 and length <= road.get_Right() + self.person.get_Gravity() :
                
                if length > road.get_Left()* (5.5/9) + road.get_Right() * (3.5/9) and length < road.get_Left()* (3.5/9) + road.get_Right() * (5.5/9):
                    self.process.state_perfect = True
                    self.game.sound_Perfect()
                    self.process.Score(2)
                else :
                    self.process.Score()

                self.num_bridge = self.road.index(road)
                return

        self.num_bridge = 0
        self.game.sound_Falling()
