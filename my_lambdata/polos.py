

class Polo:
    def __init__(self, size, color, price=69.99): # Constructor
        self.size = size
        self.color = color
        self.price = price

    def wash(self):
        print(f"WASHING THE {self.size.upper()} {self.color.upper()} POLO")

if __name__ == "__main__":
    
    
    
    polo = Polo(size = "Large", color = "Blue")
    print(polo.size, polo.color)
    polo.wash()

    polo2 = Polo(size = "Small", color = "Yellow")
    print(polo2.size, polo2.color)
    polo2.wash()
    