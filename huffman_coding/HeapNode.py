class HeapNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other) -> bool:
        return self.frequency < other.frequency

    def __gt__(self, other) -> bool:
        return self.frequency > other.frequency

    def __eq__(self, other) -> bool:
        if (other is None) or (not isinstance(other, HeapNode)):
            return False
        return self.frequency == other.frequency
