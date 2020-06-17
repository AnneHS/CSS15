from mesa import Model
from mesa.space import HexGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

import numpy as np

from agent_hexogonal import Pedestrian, Wall, Exit



class EvacuationModel(Model):

    def __init__(self, N=20, height=21, width=21, push_ratio = 0.5):
        super().__init__()
        self.height = height
        self.width = width
        self.num_agents = N

        self.exit_x = self.width - 1
        self.exit_y = round(self.height/2)

        self.push_probs = np.array([[0.,0.],[1.,0.5]])

        self.grid = HexGrid(self.width, self.height, torus=False)
        self.schedule = RandomActivation(self)

        # decide for ID whether it is a pusher
        is_pusher = np.zeros(N, dtype = int)
        idx = self.random.sample([i for i in range(N)], int(push_ratio * N))
        is_pusher[idx] = 1
        
        # Add N pedestrians
        taken_pos = []
        for i in range(self.num_agents):
            # Add the agent to a random grid cell
            while True:
                x = self.random.randrange(1, self.grid.width-1)
                y = self.random.randrange(1, self.grid.height-1)
                pos = (x,y)
                if not pos in taken_pos:
                    break
            a = Pedestrian(i, self, pos, self.exit_x, self.exit_y, is_pusher[i])
            self.schedule.add(a)

            self.grid.place_agent(a, pos)
            taken_pos.append(pos)
        print(len(taken_pos))
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

            # One exit
            if x == self.exit_x and y == self.exit_y:
                e = Exit(self, (x, y))
                #self.schedule.add(e)
                self.grid.place_agent(e, (x, y))
            else:
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


        self.data_collector = DataCollector({
            "Evacuees": lambda m: self.count_evacuees(),
            "Evacuated": lambda m: self.count_evacuated()
        })

         # this is required for the data_collector to work
        self.running = True
        self.data_collector.collect(self)

    def count_evacuees(self):
        count = self.schedule.get_agent_count()
        print('EVACUEES COUNT')
        print(count)
        print()
        return count

    def count_evacuated(self):
         count = self.num_agents - self.schedule.get_agent_count()
         return count

    def step(self):
        print(self.schedule.get_agent_count())
        if self.schedule.get_agent_count() == 0:
            exit()
        else:
            self.schedule.step()
        print("")
        self.data_collector.collect(self)





empty_model = EvacuationModel()
empty_model.step()
