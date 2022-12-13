from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for x in System._hardware:
            if x.name == hardware_name:
                express_soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
                x.install(express_soft)
                System._software.append(express_soft)
            return "Hardware does not exist"
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for x in System._hardware:
            if x.name == hardware_name:
                light_soft = LightSoftware(name, capacity_consumption, memory_consumption)
                x.install(light_soft)
                System._software.append(light_soft)
            return "Hardware does not exist"
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        for x in System._hardware:
            for y in System._software:
                if x.name == hardware_name and y.name == software_name:
                    x.uninstall(y)
                    System._software.remove(y)
                else:
                    return "Some of the components do not exist"
            return "Some of the components do not exist"
        return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum(h.memory for h in System._hardware)
        total_used_memory = sum(s.memory_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)
        total_used_space = sum(s.capacity_consumption for s in System._software)

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_space} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            express_software = [s for s in h.software_components if s.software_type == "Express"]
            light_software = [s for s in h.software_components if s.software_type == "Light"]
            total_used_memory = sum(s.memory_consumption for s in h.software_components)
            total_used_space = sum(s.capacity_consumption for s in h.software_components)
            software_names = ', '.join(x.name for x in h.software_components)
            result += f"Hardware Component - {h.name}\n" \
                      f"Express Software Components: {len(express_software)}\n" \
                      f"Light Software Components: {len(light_software)}\n" \
                      f"Memory Usage: {total_used_memory} / {h.memory}\n" \
                      f"Capacity Usage: {total_used_space} / {h.capacity}\n" \
                      f"Type: {h.TYPE}\n" \
                      f"Software Components: {software_names if software_names else 'None'}\n"
        return result


System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())
