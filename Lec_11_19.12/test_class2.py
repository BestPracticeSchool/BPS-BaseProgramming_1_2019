class Myclass:
    def __init__(self, age = 0, h= 0, w = 0, name = ""):
        print("Construct working!")
        self.Age = age
        self.H = h
        self.W = w
        self.Name = name
        print("Construct done!")

    def days_life(self) -> int:
        return self.Age * 365 


m = Myclass(28, 195, 99, "Bob")
print(m.Age, m.H, m.W, m.Name)
q = Myclass(12, 155, 55, "Rolf")
print("Q alive: ", q.days_life())
z = Myclass(name = "Timmy")
print(z.Age, z.Name)
