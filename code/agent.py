# https://github.com/Chadsr/MesaFireEvacuation
from mesa import Agent
import math

class Pedestrian(Agent):
    def __init__(self, unique_id, model, pos, exit_x, exit_y, push_type):
        super().__init__(unique_id, model)
        self.pos=pos
        self.traversable=False
        self.exit_x = exit_x
        self.exit_y = exit_y
        self.push = push_type
        self.exit_time = math.inf

    def location_is_traversable(self, pos):
        '''
        Check if cell is traversable (walls and pedestrians aren't).
        '''
        traversable=True
        if not self.model.grid.is_cell_empty(pos):
            contents = self.model.grid.get_cell_list_contents([pos])

            for agent in contents:
                if not agent.traversable:
                    if self.push > 0 and isinstance(agent, Pedestrian):
                        continue
                    else:
                        traversable = False
        return traversable

    def at_exit(self):
        '''
        Check if at exit.
        '''
        exit_reached = False
        if self.pos[0] == self.exit_x and self.pos[1] == self.exit_y:

            exit_reached = True


        return exit_reached

    def pushing(self, new_position):

        contents = self.model.grid.get_cell_list_contents([new_position])

        if len(contents) > 0:
            for agent in contents:
                if isinstance(agent, Pedestrian):
                    push_prob = self.model.push_probs[self.push, agent.push]
                    if push_prob > self.random.random():
                        print(self.push, agent.push, self.pos, agent.pos)
                        self.model.grid.move_agent(agent, self.pos)
                        self.model.grid.move_agent(self, new_position)
                    return

        self.model.grid.move_agent(self, new_position)


    def move(self):

        if self.at_exit():
            print(str(self.unique_id) + " has exited")

            self.exit_time = self.model.schedule.time
            self.model.exit_times.append(self.exit_time)

            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)

        else:

            # Possible steps in neighborhood
            possible_steps = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=True)

            # Traversable steps
            # TODO: faster
            traversable_steps=[]
            for step in possible_steps:
                if self.location_is_traversable(step):
                    traversable_steps.append(step)

            if len(traversable_steps) > 0:
                # move toward exit - add types of movement later

                #this should be automatic
                #self.exit_x = round(11/2)
                #self.exit_y = 10

                traversable_steps.append(self.pos)
                steps = [max(abs(self.exit_x-candidate[0]), abs(self.exit_y-candidate[1])) for candidate in traversable_steps]
                #steps that produce shortest possible path
                min_steps = min(steps)
                potential = [traversable_steps[i] for i in range(len(steps)) if steps[i]==min_steps]
                #avoid zig-zagging
                potential2 = [i for i in potential if (abs(i[0]-self.exit_x)-abs(self.pos[0]-self.exit_x))<1]
                if (len(potential2)>0):
                    potential = potential2


                new_position = self.random.choice(potential)
                #print("if")
                #print(self.unique_id)
                #print(self.pos)
                self.pushing(new_position)
                #print(self.pos)
                #print()
                #self.pos = new_position
            else:
                #not needed?
                self.model.grid.move_agent(self, self.pos)
                #print(self.pos)
                #print()
        #print ("pos:", self.pos)


    def step(self):

        self.move()




class Wall(Agent):
    def __init__(self, model, pos):
        super().__init__(model, pos)
        self.traversable=False


class Exit(Agent):
    def __init__(self, model, pos):
        super().__init__(model, pos)
        self.traversable=True
