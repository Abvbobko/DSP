import pandas as pd
from data.data import a, b, v, g


class DataStorage:

    NUM_OF_OPTIONS = 6

    def __init__(self, data_a, data_b, data_v, data_g):
        self._table_a = DataStorage.create_df(data_a, index_name='option')
        self._table_b = DataStorage.create_df(data_b, index_name='option')
        self._table_v = DataStorage.create_df(data_v, index_name='option')
        self._table_g = [
            DataStorage.generate_table_g(
                A=data_g['A'][i],
                j=5,
                phi=data_g['phi'][i]
            ) for i in range(6)
        ]

    @staticmethod
    def create_df(data, index_name=None, num_of_options=NUM_OF_OPTIONS):
        df = pd.DataFrame(
            data=data,
            index=[option for option in range(1, num_of_options + 1)]
        )
        if index_name:
            df.index.name = index_name
        return df

    @staticmethod
    def generate_table_g(A, j, phi):
        data = {
            'A': [A] * j,
            'f': [i for i in range(1, j+1)],
            'phi': phi
        }
        return DataStorage.create_df(data=data, index_name='j', num_of_options=j)

    def get_a(self, option=None):
        if not option:
            return self._table_a
        if option in self._table_a.index:
            return self._table_a.loc[option]
        return None

    def get_b(self, option=None):
        if not option:
            return self._table_b
        if option in self._table_b.index:
            return self._table_b.loc[option]
        return None

    def get_v(self, option=None):
        if not option:
            return self._table_v
        if option in self._table_v.index:
            return self._table_v.loc[option]
        return None

    def get_g(self, option=None):
        if not option:
            return self._table_g
        if (option-1) < len(self._table_g):
            return self._table_g[option - 1]
        return None


def generate_data():
    return DataStorage(data_a=a, data_b=b, data_v=v, data_g=g)
