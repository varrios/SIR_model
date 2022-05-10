class Relationship:
    def __init__(self, kto, z_kim, moc_relacji):
        self.kto = kto
        self.z_kim = z_kim
        self.moc_relacji = moc_relacji


class Relationships:
    def __init__(self, n=10_000):
        self.n = n
        self.relationships = []

    def import_data(self, file_name):
        with open(file_name) as file:
            dane = file.read().splitlines(False)
            for line in dane:
                kto, z_kim, moc_relacji = line.split(",")
                new_relation = Relationship(int(kto), int(z_kim), float(moc_relacji))
                self.relationships.append(new_relation)

    def is_in_relation(self, n1, n2):
        for element in self.relationships:
            if element.kto == n1 and element.z_kim == n2:
                return True
        return False

    def get_all_neighbours(self, n):
        for element in self.relationships:
            if element.kto == n:
                yield element.kto
