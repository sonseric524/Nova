
#### main.py

```python
#!/usr/bin/env python3
import random

conditions = [
    "Sunny", "Cloudy", "Rainy", "Windy", "Stormy", "Snowy", "Foggy"
]

def generate_forecast():
    condition = random.choice(conditions)
    temperature = round(random.uniform(-10, 35), 1)  # Temperature in Celsius
    return condition, temperature

def main():
    print("Welcome to Nova Weather Forecast!")
    condition, temperature = generate_forecast()
    print(f"Today's weather: {condition} with a temperature of {temperature}°C")

if __name__ == "__main__":
    main()
