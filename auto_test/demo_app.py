def check_sensor(sensor):
    """Check the status of the given sensor"""
    if sensor["value"] >= sensor["minimum"]:
        return "PASS"
    else:
        return "FAIL"

def main():
    # list: define sensors
    sensors = [
        {"name": "Side 1 load cell", "value": 50, "minimum": 10},
        {"name": "Side 2 load cell", "value": 5, "minimum": 10},
    ]
    # for loop to check each sensor's status
    for sensor in sensors:
        result = check_sensor(sensor)
        print(f"Sensor {sensor['name']} status: {result}")

if __name__ == "__main__":
    main()