# https://github.com/Chadsr/MesaFireEvacuation
from mesa import Agent

class Pedestrian(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        #self.unique_id = unique_id
        self.pos=pos
        self.traversable=False

    def location_is_traversable(self, pos):
        '''
        Check if cell is traversable (walls aren't).
        '''
        traversable=True
        if not self.model.grid.is_cell_empty(pos):
            contents = self.model.grid.get_cell_list_contents([pos])
            #print(self.unique_id)
            for agent in contents:
                #print(type(agent))
                if not agent.traversable:
                    traversable=False
        #print()

        return traversable

    def at_exit(self):
        '''
        Check if at exit.
        '''
        exit_reached = False
        #print(self.unique_id)
        #print("At exit")
        #print(self.pos)
        #print()
        if not self.model.grid.is_cell_empty(self.pos):
            contents = self.model.grid.get_cell_list_contents([self.pos])
            #print(contents)

            for agent in contents:
                if isinstance(agent, Exit):
                    exit_reached = True

        return exit_reached

    def move(self):

        if self.at_exit():
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)

        else:

            # Possible steps in neighborhood
            possible_steps = self.model.grid.get_neighborhood(
                self.pos,
                moore=True,
                include_center=False)

            # Traversable steps
            # TODO: faster
            traversable_steps=[]
            for step in possible_steps:
                if self.location_is_traversable(step):
                    traversable_steps.append(step)

            if len(traversable_steps) > 0:
                # Random move
                new_position = self.random.choice(traversable_steps)
                self.model.grid.move_agent(self, new_position)
            else:
                self.model.grid.move_agent(self, self.pos)


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
