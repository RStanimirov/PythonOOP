from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_memory = self.memory - sum(x.memory_consumption for x in self.software_components)
        self.available_capacity = self.capacity - sum(x.capacity_consumprion for x in self.software_components)

    # @property
    # def available_memory(self):
    #     return self.memory-sum(s.memory_consumption for s in self.software_components)
    #
    # @property
    # def available_capacity(self):
    #     return self.capacity-sum(s.capacity_consumption for s in self.software_components)

    def install(self, software: Software):
        if software.capacity_consumption > self.available_capacity \
                or software.memory_consumption > self.available_memory:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)


# hard = Hardware("H", "Heavy", 100, 100)
# print(hard.__dict__)