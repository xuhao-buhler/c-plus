import pytest

def pytest_configure(config):
    """Register custom markers for pytest"""
    config.addinivalue_line(
        "markers", "run(order): mark test to run in specified order"
    )

def pytest_collection_modifyitems(config, items):
    """Modify the order of test items based on the 'run' marker"""
    def get_order(item):
        marker = item.get_closest_marker("run")
        if marker is None:
            return float('inf')

        return marker.kwargs.get("order", float('inf'))

    items.sort(key=get_order)

def pytest_runtest_setup(item):
    """Hook to run before each test item is executed"""
    print(f"Setting up test: {item.name}\n")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to modify the test report for each test item"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            print(f"[RESULT] {item.name} passed\n")
        elif report.failed:
            print(f"[RESULT] {item.name} failed\n")
            print(f"[ACTION] {item.name} test failed\n")
        elif report.skipped:
            print(f"[RESULT] {item.name} skipped\n")

def pytest_runtest_teardown(item, nextitem):
    """Hook to run after each test item is executed"""
    print(f"Tearing down test: {item.name}\n")