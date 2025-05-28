class Electric:
    def start_engine():
        print("Electric engine starts silently...")

class Gas:
    def start_engine():
        print("Gas engine starts with noise...")

class HybridCar(Electric, Gas):  # Multiple inheritance
    pass

#h = HybridCar()
HybridCar.start_engine()  # Which one runs? Electric or Gas?
