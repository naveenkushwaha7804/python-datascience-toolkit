# ============================================================
# POLYMORPHISM - RUNTIME POLYMORPHISM
# ============================================================

class Human:
    def sound(self):
        print("Human sound")


class Animal:
    def sound(self):
        print("Animal sound")


objects = [Human(), Animal()]

for obj in objects:
    obj.sound()