class Operations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b  # <--- fix this in step 7

    def multiply(self, a, b):
        return a * b

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        return self.multiply(self.subtract(fahrenheit, 32), 5 / 9) # <-- Fix this in step 7