# https://github.com/Chadsr/MesaFireEvacuation
from mesa import Agent

class Pedestrian(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        #self.unique_id = unique_id
        self.pos=pos
        self.traversable=False

    def location_is_traversable(self, pos):

        # Check if location traversable
        if not self.model.grid.is_cell_empty(pos):
            contents = self.model.grid.get_cell_list_contents([self.pos])
            for agent in contents:
                if not agent.traversable:
                    return False

        return True


    def move(self):

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

        # Random move
        new_position = self.random.choice(traversable_steps)
        self.model.grid.move_agent(self, new_position)


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
