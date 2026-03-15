"""Core functionality of ABC Library"""

class A1:
    """Class A1 - Core component of ABC Library"""

    def __init__(self, value):
        self.value = value

    def function_a(self, a: float, b: float):
        """Example function in Class A1"""
        return f"Function a called with value: {self.value, a, b}"

    def function_b(self):
        """Another example function in Class A1"""
        return f"Function b called with value: {self.value}"

class A2:
    """Class A2 - Core component of ABC Library"""

    def __init__(self, value):
        self.value = value

    def function_c(self, x: int):
        """Example function in Class A2"""
        return f"Function c called with value: {self.value, x}"

    def function_d(self):
        """Another example function in Class A2"""
        return f"Function d called with value: {self.value}"
