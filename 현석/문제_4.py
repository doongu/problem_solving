import numpy


class Paper:
    def __init__(self, width: int, colors: numpy.ndarray):
        self.__width = width
        self.__color_data = colors

    def __is_single_color(self):
        return numpy.all(self.__color_data == self.__color_data[0, 0])

    def get_color(self):
        if not self.__is_single_color():
            raise Paper.NotSingleColorException()
        return self.__color_data[0, 0]

    def cut(self):
        half_width = self.__width // 2
        color_data_arrays = [
            self.__color_data[:half_width, :half_width],
            self.__color_data[:half_width, half_width:],
            self.__color_data[half_width:, :half_width],
            self.__color_data[half_width:, half_width:]
        ]
        return [Paper(half_width, color_data) for color_data in color_data_arrays]

    class NotSingleColorException(Exception):
        pass


class Case:
    def __init__(self, paper: Paper):
        self.__paper = paper
        self.__counts = {0: 0, 1: 0}
        self.__solve()

    def __solve(self):
        try:
            color = self.__paper.get_color()
            self.__counts[color] += 1
        except Paper.NotSingleColorException:
            papers = self.__paper.cut()
            for paper in papers:
                case = Case(paper)
                counts = case.get_counts()
                self.__counts[0] += counts[0]
                self.__counts[1] += counts[1]

    def get_counts(self):
        return self.__counts


class FileInput:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__case = None
        self.__deserialize()

    def __deserialize(self):
        with open(self.__file_name, "r") as f:
            width = int(f.readline())
            color_data = []
            for i in range(width):
                color_data.append(list(map(int, f.readline().split())))
            paper = Paper(width, numpy.array(color_data))
            self.__case = Case(paper)

    def get_case(self):
        return self.__case


case = FileInput("./input.txt").get_case()
print(case.get_counts())
