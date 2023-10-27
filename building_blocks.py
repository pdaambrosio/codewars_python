# > A class that represents a block with a width, length, and height.
class Block:
    def __init__(self, values: list):
        self.values = values
        self.width = values[0]
        self.length = values[1]
        self.height = values[2]
    
    def get_width(self) -> int:
        return self.width

    def get_length(self) -> int:
        return self.length

    def get_height(self) -> int:
        return self.height

    def get_volume(self) -> int:
        return self.width * self.length * self.height

    def get_surface_area(self) -> int:
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)


def main() -> None:
    b = Block([2, 4, 6])
    print(b.get_width())  # 2
    print(b.get_length())  # 4
    print(b.get_height())  # 6
    print(b.get_volume())  # 48
    print(b.get_surface_area())  # 88
    

if __name__ == '__main__':
    main()
