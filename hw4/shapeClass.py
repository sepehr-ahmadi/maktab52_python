from abc import abstractmethod, ABC


class shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def environment(self):
        pass

    @abstractmethod
    def area(self):
        pass


class rectangle(shape):
    def __init__(self, environment, area):
        self._environment = environment
        self._area = area

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, new_environment):
        self._environment = new_environment

    @environment.getter
    def environment(self):
        return self._environment

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new_area):
        self._area = new_area

    @area.getter
    def area(self):
        return self._area

    def draw(self):
        pass


class squre(shape):
    def environment(self):
        pass

    def area(self):
        pass

    def draw(self):
        pass
    def draw_concat(list_sides):
        counter = 0
        for j in range(max(list_sides)):
            counter += 1
            for i in list_sides:
                if counter > i:
                    print(' ' * i, end='')
                else:
                    print('*' * i, end='')
            print()




    # def draw_concat(squrelis):
    #     squers_list = squrelis
    #     print(squrelis)
    #     for i in range(1, max(squers_list) + 1):
    #         for j in range(1, sum(squers_list) + 1):
    #             if i <= squers_list[0] and j <= squers_list[0]:
    #                 print("*", end=" ")
    #             elif i <= squers_list[1] and squers_list[1] + squers_list[0] >= j > squers_list[0]:
    #                 print("*", end=" ")
    #             elif i <= squers_list[2] and squers_list[2] + squers_list[0] + squers_list[1] >= j > squers_list[0] + \
    #                     squers_list[1]:
    #                 print("*", end=" ")
    #             else:
    #                 print(" ", end=" ")
    #         print()


rec = rectangle(5, 15)
print(rec.area)
squ = squre
squ.draw_concat([2, 5, 3])
