from mesa import Model
from mesa.space import HexGrid
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

import numpy as np
import math
import matplotlib.pyplot as plt

from agent_merge import Pedestrian, Wall



class EvacuationModel(Model):

    def __init__(self, N=20, height=21, width=21, hexogonal=True, push_ratio = 0.5):
        super().__init__()
        self.height = height
        self.width = width
        self.num_agents = N
        self.hex = hexogonal

        self.exit_x = self.width - 1
        self.exit_y = round(self.height/2)

        self.push_probs = np.array([[0.,0.],[1.,0.5]])

        self.exit_times=[]

        if self.hex:
            self.grid = HexGrid(self.width, self.height, torus=False)
        else:
            self.grid = MultiGrid(self.width, self.height, torus=False)

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

        # Place vertical walls
        for i in range(self.height):

            
            X=[0, self.width - 1]
            y=i

            # Left and right
            for x in X: 
                if not (x == self.exit_x and y == self.exit_y):
                    w = Wall(self, (x, y))
                    self.grid.place_agent(w, (x, y))

        # Place horizontal walls
        for i in range(self.width):

            x=i
            Y=[0, self.height - 1]

            # Up and down
            for y in Y:
                if not (x == self.exit_x and y == self.exit_y):
                    w = Wall(self, (x, y))
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
        return count

    def count_evacuated(self):
         count = self.num_agents - self.schedule.get_agent_count()
         return count

    def plot(self):

        # Average exit time
        sum=0
        for time in self.exit_times:
            sum+=time
        avg = sum/len(self.exit_times)

        # Exit times bins
        L = self.exit_times[-1] - 0
        bin_size = 5
        min_edge = 0
        max_edge = math.ceil(L/bin_size) * bin_size
        N = int((max_edge-min_edge)/bin_size)
        Nplus1 = N+1
        bin_list = np.linspace(min_edge, max_edge, Nplus1)

        print()
        print(self.exit_times)
        print(L)
        print(max_edge)
        print()
        # Exit times histogram
        plt.hist(self.exit_times, bin_list, edgecolor="k")
        plt.title("Average = " + str(avg))
        plt.xlabel("Exit time")
        plt.ylabel("Frequence")
        plt.show()

        return

    def step(self):

        # Stop run if all Pedestrians have exited
        if self.schedule.get_agent_count() == 0:
            self.plot()
            self.running=False

        self.schedule.step()
        self.data_collector.collect(self)