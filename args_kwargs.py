def describe_car(brand, model, **features):
    print(f"Car: {brand} {model}")
    for key, value in features.items():
        print(f"{key}: {value}")


describe_car("Tesla", "Model 3", color="red", autopilot=True)
