# Process based nodes
from beagle.edges import Edge


class Launched(Edge):
    __name__ = "Fork"

    timestamp: int  # Array of process launch times

    def __init__(self) -> None:
        super().__init__()
        
