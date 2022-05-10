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
        self.n_agents = 10000
        self.relationships = relations.Relationships()
        self.relationships.import_data(filename)
        self.agents = self.create_agents(self.n_agents)
        self.constants = constants
        self.new_states = [State.Susceptible for i in range(self.n_agents)]
        # TODO: set proper values
        self.n_agents_susceptible = self.n_agents
        self.n_agents_infected = 0
        self.n_agents_recovered = 0
        self.initialized = False
        self.set_infected_agents()

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

    def run_simulation(self):
        self.log_data()
        n_steps = 10
        for i in range(n_steps):
            print("Running simulation step", i)
            self.sim_step(i)

    def sim_step(self,n_step):
        self.agents_spread_disease()
        self.agents_recover()
        self.log_data()

    def set_infected_agents(self):
        for i in range(500):
            self.agents[i].state = State.Infected
        self.n_agents_infected = 500
        self.n_agents_susceptible -= 500

    def log_data(self):
        if not self.initialized:
            with open("sim_data.txt", "w") as new:
                new.write("Susceptible,Infected,Recovered")
                new.write("\n")
                new.write(f"{self.n_agents_susceptible},{self.n_agents_infected},{self.n_agents_recovered}")
                new.write("\n")
                self.initialized = True
        else:
            with open("sim_data.txt", "a") as new:
                new.write(f"{self.n_agents_susceptible},{self.n_agents_infected},{self.n_agents_recovered}")
                new.write("\n")

    def agents_recover(self):
        for agent in self.agents:
            if agent.state == State.Infected:
                if random.random() < 0.5:
                    agent.state = State.Recovered
                    self.n_agents_infected -=1
                    self.n_agents_recovered +=1

    def agents_spread_disease(self):
        for i,agent in enumerate(self.agents):
            if agent.state == State.Infected:
                neighbours = self.relationships.get_all_neighbours(i)
                for neighbour in neighbours:
                    if random.random() < 0.5:
                        self.new_states[neighbour] = State.Infected
                        self.n_agents_susceptible -=1
                        self.n_agents_infected +=1
        for i in range(self.n_agents):
            self.agents[i].state = self.new_states[i]
