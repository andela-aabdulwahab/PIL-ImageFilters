class BoundedValue(object):

    def __init__(self, value, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.set(value)

    def set(self, newValue):
        self.value = max(self.min_value, min(self.max_value, newValue))
        return self

    def __str__(self):
        return str(self.value)
