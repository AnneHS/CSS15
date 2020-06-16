from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation

from agent import Pedestrian, Wall, Exit

class EvacuationModel(Model):

    def __init__(self, N=10, height=21, width=21):
        super().__init__()
        self.height = height
        self.width = width
        self.num_agents = N

        self.exit_x = round(self.width/2)
        self.exit_y = self.height-1

        self.grid = MultiGrid(self.width, self.height, torus=False)
        self.schedule = RandomActivation(self)



        # Add N pedestrians
        for i in range(self.num_agents):

            # Add the agent to a random grid cell
            x = self.random.randrange(1, self.grid.width-1)
            y = self.random.randrange(1, self.grid.height-1)

            a = Pedestrian(i, self, (x, y))
            self.schedule.add(a)

            self.grid.place_agent(a, (x, y))

        # Place vertical walls
        for i in range(self.height):

             # Left
            x=0
            y=i
            w = Wall(self, (x, y))
            #self.schedule.add(w)
            self.grid.place_agent(w, (x, y))

            # Right
            x=self.width-1
            y=i
            w = Wall(self, (x, y))
            #self.schedule.add(w)
            self.grid.place_agent(w, (x, y))

        # Place horizontal walls
        for i in range(self.width):

            # Up
            x=i
            y=0
            w = Wall(self, (x, y))
            #self.schedule.add(w)
            self.grid.place_agent(w, (x, y))

            # Down
            x=i
            y=self.height-1

            # One exit
            if x == self.exit_x and y == self.exit_y:
                e = Exit(self, (x, y))
                #self.schedule.add(e)
                self.grid.place_agent(e, (x, y))
            else:
                w = Wall(self, (x, y))
                #self.schedule.add(w)
                self.grid.place_agent(w, (x, y))



    def step(self):
        self.schedule.step()

empty_model = EvacuationModel()
empty_model.step()
