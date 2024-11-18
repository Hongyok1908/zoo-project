class Zoo:
    def get_ticket_price(self, age):
        if age <= 0:
            return "Age must be more than zero"
        if 0 < age <= 12:      
            return 50
        elif 12 < age <= 20:   
            return 100
        elif 20 < age <= 60:   
            return 150
        else:         
            return 100
        

if __name__ == "__main__":
    zoo = Zoo()
    print("Zoo ticket prices : ")
    test_ages = [5, 15, 30, 70, -1]
    
    for age in test_ages:
        try:
            price = zoo.get_ticket_price(age)
            print(f"Age {age}: {price} baht")
        except ValueError as e:
            print(f"Age {age}: {e}")