class ElectronicComponent:
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_unit(self):
        return self.unit

    def __str__(self):
        return f"Компонент: {self.value} {self.unit} ({self.name})"


# Порожній клас ComponentManager 
class ComponentManager:
    pass


class ElectronicInventory(ElectronicComponent, ComponentManager):
    def __init__(self):
        # Інвентар зберігає список компонентів
        self.inventory = []

    def add_component(self, component):
        if isinstance(component, ElectronicComponent):
            self.inventory.append(component)
        else:
            raise TypeError("Можна додавати лише об'єкти ElectronicComponent")

    def get_all_components(self):
        return self.inventory

    def find_component_by_name(self, name):
        return [c for c in self.inventory if c.get_name().lower() == name.lower()]

    def remove_component(self, name):
        before_count = len(self.inventory)
        self.inventory = [c for c in self.inventory if c.get_name().lower() != name.lower()]
        return before_count - len(self.inventory)  # кількість видалених

    def get_component_count(self):
        return len(self.inventory)

    def __str__(self):
        if not self.inventory:
            return "Інвентар порожній"
        return "\n".join(str(component) for component in self.inventory)
# Створення компонентів
resistor = ElectronicComponent("Резистор", "10k", "Ом")
capacitor = ElectronicComponent("Конденсатор", "100", "нФ")

# Створення інвентаря
inventory = ElectronicInventory()

# Додавання компонентів
inventory.add_component(resistor)
inventory.add_component(capacitor)

# Виведення всіх компонентів
print("=== Всі компоненти ===")
print(inventory)

# Пошук компоненту
print("\n=== Пошук 'Резистор' ===")
for comp in inventory.find_component_by_name("Резистор"):
    print(comp)

# Видалення компоненту
inventory.remove_component("Конденсатор")

# Після видалення
print("\n=== Після видалення ===")
print(inventory)


