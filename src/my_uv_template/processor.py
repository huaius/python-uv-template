class Processor:
    """Main module

    """


    def __init__(self, number1: str, number2: str) -> None:
        self.number1 = number1
        self.number2 = number2

    def run(self) -> int:
        """Perform the analysis"""
        return int(self.number1) + int(self.number2)
 