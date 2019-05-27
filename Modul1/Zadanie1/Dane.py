import random
import numpy as np


class Dane:
    def POBIERZ(self, filename, separator):
        error = False
        try:
            f = open(filename, "r")
        except IOError:
            print("Nie udało się otworzyć pliku o podannej ścieżce")
            error = True
        if error == False:
            array = []
            for i in f.readlines():

                for j in i.split(separator):
                    array.append(j.strip())

            print(array)

    def TASUJ(self, input_list):
        reshuffled_list = []
        n = len(input_list)
        for i in range(n):
            index = random.randint(0, len(input_list) - 1)
            reshuffled_list.append(input_list[index])
            input_list.pop(index)

        print(reshuffled_list)

    def NORMALIZUJ(self, input_list, method="minmax"):
        if method is "minmax":
            # Get minimum and maximum from input values
            minimum = min(input_list)
            maximum = max(input_list)
            for i in range(len(input_list)):
                # change values with equation x = (x-min)/(max-min)
                input_list[i] = (input_list[i] - minimum) / (maximum - minimum)
            print(input_list)
        elif method is "standaryzacja":
            # Convert pytohn array to numpy array
            input_list = np.array(input_list)
            # Calculate values in array with equation  y = (x-mean/standard)
            input_list = (input_list - input_list.mean()) / input_list.std()
            print(input_list)
        elif method is "mean":

            maximum = max(input_list)
            minimum = min(input_list)
            mean = sum(input_list) / float(len(input_list))
            for i in range(len(input_list)):
                input_list[i] = (input_list[i] - mean) / (maximum - minimum)
            print(input_list)


d = Dane()
d.POBIERZ("test1.txt", ",")
d.TASUJ([1, 2, 3, 4, 5, 6])
d.NORMALIZUJ([1, 2, 3, 4, 3, 2, 1, 4], "minmax")
d.NORMALIZUJ([1, 2, 3, 4, 3, 2, 1, 4], "standaryzacja")
d.NORMALIZUJ([1, 2, 3, 4, 3, 2, 1, 4], "mean")

