class ClassName:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


c1 = ClassName("Alice")
c1.greet()
