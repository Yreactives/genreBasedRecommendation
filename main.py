import pandas
from math import sqrt
from os import path
class simple_knn:
    def __init__(self, data:path, data2:path=None):
        if not data2:
            self.df_data = pandas.read_excel(data)
            self.df_eval = pandas.read_excel(data, sheet_name=1)
        else:
            self.df_data = pandas.read_excel(data)
            self.df_eval = pandas.read_excel(data2)

    def data_sort(self, arg: dict):
        return dict(sorted(arg.items(), key=lambda item : item[1]))

    def knn(self, tags):
        distances = {}
        for i in range(len(self.df_data.index)):
            a = 0
            for j in range(len(tags)):
                a += (self.df_data.loc[i, tags[j]] - self.df_eval.loc[0, tags[j]]) ** 2

            distances[i] = sqrt(a)

        return distances

    def tags_extraction(self):
        num = 1
        tags = []
        while True:
            try:
                tags.insert(num-1, self.df_eval.columns[num])
                num += 1
            except:
                break
        return tags

    def calculate(self):
        #euclidean distance


        tags = self.tags_extraction()

        distances = self.knn(tags)

        distances_sorted = self.data_sort(distances)

        num = 0
        output = []
        for key, values in distances_sorted.items():
            #print(f"rank {num}: ", end="")
            #print(self.df_data.loc[key, "Nama Barang"], end="\n")
            output.insert(num, self.df_data.loc[key, "Nama Barang"])
            num += 1

        return output


calculation_output = simple_knn("sample.xlsx").calculate()

rank = 1
for i in calculation_output:
    print(f"rank {rank}: ", end="")
    print(i)
    rank += 1


