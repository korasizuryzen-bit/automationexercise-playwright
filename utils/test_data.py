import time


def unique_email() -> str:
    return f"test_{int(time.time())}@mailinator.com"
