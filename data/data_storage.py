import pandas as pd
from data.data import a, b, v, g


class DataStorage:

    NUM_OF_OPTIONS = 6

    def __init__(self, data_a, data_b, data_v, data_g):
        self._table_a = DataStorage.create_df(data_a)
        self._table_b = DataStorage.create_df(data_b)
        self._table_v = DataStorage.create_df(data_v)
        self._table_g = [DataStorage.generate_table_g(A=data_g['A'][i], phi=data_g['phi'][i]) for i in range(6)]

    @staticmethod
    def create_df(data, num_of_options=NUM_OF_OPTIONS):
        df = pd.DataFrame(
            data=data,
            index=[option for option in range(1, num_of_options + 1)]
        )
        df.index.name = 'option'
        return df

    @staticmethod
    def generate_table_g(A, phi):
        data = {
            'j': [i for i in range(1, 6)],
            'Aj': [A] * 5,
            'fj': [i for i in range(1, 6)],
            'phi_j': phi
        }
        return DataStorage.create_df(data=data, num_of_options=5)

    def get_a(self, option):
        if option in self._table_a.index:
            return self._table_a.loc[option]
        return None

    def get_b(self, option):
        if option in self._table_b.index:
            return self._table_b.loc[option]
        return None

    def get_v(self, option):
        if option in self._table_v.index:
            return self._table_v.loc[option]
        return None

    def get_g(self, option):
        if (option-1) < len(self._table_g):
            return self._table_g[option - 1]
        return None


def generate_data():
    return DataStorage(data_a=a, data_b=b, data_v=v, data_g=g)
