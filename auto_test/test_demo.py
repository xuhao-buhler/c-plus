import pytest
from demo_app import check_sensor

@pytest.mark.run(order=1)
def test_sensor_value_passes():
    sensor = {"name": "Side 1 load cell", "value": 50, "minimum": 10}
    
    assert check_sensor(sensor) == "PASS"
@pytest.mark.run(order=2)
def test_sensor_value_fails():
    sensor = {"name": "Side 2 load cell", "value": 5, "minimum": 10}
    
    assert check_sensor(sensor) == "FAIL"