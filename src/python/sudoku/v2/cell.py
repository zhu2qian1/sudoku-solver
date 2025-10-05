class Cell:
    def __init__(self, value: int = 0, memo: set[int] = set()):
        if value < 0:
            raise ValueError("Cell value cannot be negative")
        self.value = value
        self.memo = memo

    def __str__(self):
        return str(self.value) if self.value else "_"
