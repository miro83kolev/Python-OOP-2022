from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def find_instance_by_name(name, collection):
        for instance in collection:
            if instance.name == name:
                return instance
        return None

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        # using find by name you find the required hardware
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        # if it is none
        if hardware is None:
            return "Hardware does not exist"
        # if not install express_software add to hardware and to software
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        if hardware is None:
            return "Hardware does not exist"
        light_soft = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_soft)
        System._software.append(light_soft)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        # find hardware by name
        hardware = System.find_instance_by_name(hardware_name, System._hardware)
        # find software by name
        software = System.find_instance_by_name(software_name, System._software)
        # if both are none
        if hardware is None and software is None:
            return "Some of the components do not exist"
        # otherwise uninstall and remove from sf list
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        # find total hardware capacity
        total_hardware_capacity = sum([hw.capacity for hw in System._hardware])
        # find total hardware memory
        total_hardware_memory = sum([hw.memory for hw in System._hardware])
        # find total software capacity taken
        capacity_taken = sum([sw.capacity_consumption for sw in System._software])
        # find total software memory consumption taken
        memory_taken = sum([sw.memory_consumption for sw in System._software])

        output = f"System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {memory_taken} / {total_hardware_memory}\n" \
                 f"Total Capacity Taken: {capacity_taken} / {total_hardware_capacity}"
        return output

    @staticmethod
    def system_split():
        output = ""

        for hardware in System._hardware:
            # find all express sf installed in list of sw
            express_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Express"]
            # find all light sf installed in list of sw
            light_software_installed = [sw for sw in hardware.software_components if sw.software_type == "Light"]
            # find memory usage from all sw in hardware.sw components.
            memory_usage = sum([sw.memory_consumption for sw in hardware.software_components])
            # find capacity usage from all sw in hardware.sw components.
            capacity_usage = sum([sw.capacity_consumption for sw in hardware.software_components])
            # find sw components names from all sw in hardware.sw components.
            software_components_names = [sw.name for sw in
                                         hardware.software_components] if hardware.software_components else "None"

            output += f"Hardware Component - {hardware.name}\n"
            output += f"Express Software Components: {len(express_software_installed)}\n"
            output += f"Light Software Components: {len(light_software_installed)}\n"
            output += f"Memory Usage: {memory_usage} / {hardware.memory}\n"
            output += f"Capacity Usage: {capacity_usage} / {hardware.capacity}\n"
            output += f"Type: {hardware.hardware_type}\n"
            output += f"Software Components: {', '.join(software_components_names)}\n"

        return output.strip()




