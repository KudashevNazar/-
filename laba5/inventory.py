# Інвентар зі слотами та стаками


class Inventory:
    def __init__(self, title, max_slots, stack_size):
        self.title = title
        self.max_slots = max_slots
        self.stack_size = stack_size
        self.slots = []  # кожен слот: [назва, кількість]

    def count(self, name):
        """Скільки всього предметів з такою назвою."""
        total = 0
        for slot in self.slots:
            if slot[0] == name:
                total += slot[1]
        return total

    def free_space(self, name):
        """Скільки ще штук цього предмета влізе."""
        space = 0
        for slot in self.slots:
            if slot[0] == name:
                space += self.stack_size - slot[1]
        space += (self.max_slots - len(self.slots)) * self.stack_size
        return space

    def add(self, name, amount=1):
        """Додає предмет. Повертає True, якщо вдалося, і False, якщо немає місця."""
        if self.free_space(name) < amount:
            return False
        while amount > 0:
            placed = False
            for slot in self.slots:
                if slot[0] == name and slot[1] < self.stack_size:
                    slot[1] += 1
                    amount -= 1
                    placed = True
                    break
            if not placed:
                self.slots.append([name, 1])
                amount -= 1
        return True

    def remove(self, name, amount=1):
        """Забирає предмет. Повертає True, якщо вдалося, і False, якщо його не вистачає."""
        if self.count(name) < amount:
            return False
        while amount > 0:
            for slot in self.slots:
                if slot[0] == name:
                    slot[1] -= 1
                    amount -= 1
                    if slot[1] == 0:
                        self.slots.remove(slot)
                    break
        return True

    def show(self):
        print("---", self.title, f"({len(self.slots)}/{self.max_slots} слотів) ---")
        if len(self.slots) == 0:
            print("  (порожньо)")
        number = 1
        for slot in self.slots:
            print(f"  {number}. {slot[0]} x{slot[1]}/{self.stack_size}")
            number += 1