import relations
from enum import Enum
import random


class State(Enum):
    Susceptible = 1
    Infected = 2
    Recovered = 3


class Agent:
    def __init__(self, age):
        self.age = age
        self.state = State.Susceptible

    def change_state(self, new_state):
        self.state = new_state


class Simulation:
    def __init__(self,filename,constants):
        self.relationships = relations.Relationships()
        self.relationships.import_data(filename)
        self.agents = self.create_agents(10_000)
        self.constants = constants

    def create_agents(self, n_agents):
        result = []
        for i in range(n_agents):
            new_agent = Agent(random.randint(20,60))
            result.append(new_agent)
        return result

    def add_agents(self, n_agents):
        for i in range(n_agents):
            new_agent = Agent(random.randint(20,60))
            self.agents.append(new_agent)

    def sim_step(self,n_step):
        self.agents_spread_disease()
        self.agents_recover()

    def agents_recover(self):
        pass

    def agents_spread_disease(self):
        pass