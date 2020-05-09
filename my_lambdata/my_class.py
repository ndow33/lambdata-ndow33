

class Home:
    def __init__(self, kind, sq_ft, city, price):              
        self.kind = kind
        self.sq_ft = sq_ft
        self.city = city
        self.price = price
    
    def price_sq_ft(self):
        # Computes the price per square foot of the home
        answer = self.price/self.sq_ft
        print(f"This home costs ${answer:.2f} per square foot")


if __name__ == "__main__":

    home = Home(kind = 'Apartment', sq_ft = 1000, city = "Salt Lake City", price = 340000)
    print("Square feet: ", home.sq_ft)
    print("Home type: ", home.kind)
    home.price_sq_ft()



        