class Agent:
    def __init__(self, age):
        self.age = age
        self.state = "healthy"

    def change_state(self, new_state):
        self.state = new_state

class Relationships:
    def import_data(self):
        pass
    def is_in_relation(self,n1,n2):
        pass
    def get_all_neighbours(self,n):
        pass