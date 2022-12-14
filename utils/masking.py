""" impyute.dataset.corrupt """
import numpy as np


class Masking:
    """ Adds missing values to a complete dataset.
    Attributes
    ----------
    data: np.ndarray
        Matrix of values with no NaN's that you want to add NaN's to.
    percentage: float (optional)
        The percentage of null values you want in your dataset, a number
        between 0 and 1.
    Methods
    -------
    mcar()
        Overwrite values with MCAR placed NaN's.
    mar()
        Overwrite values with MAR placed NaN's.
    mnar()
        Overwrite values with MNAR placed NaN's.
    """
    def __init__(self, data, percentage=0.2, dtype=np.float):
        self.dtype = data.dtype
        self.shape = np.shape(data)
        self.data = data.astype(dtype)
        self.percentage = percentage

    def mcar(self):
        """ Overwrites values with MCAR placed NaN's """
        data_1d = self.data.flatten()
        n_total = len(data_1d)
        nan_x = np.random.choice(range(n_total),
                                  size=int(self.percentage*n_total),
                                  replace=False)
        for x_i in nan_x:
            data_1d[x_i] = np.nan
        output = data_1d.reshape(self.shape)
        return output

    def mar(self):
        """ Overwrites values with MAR placed NaN's """
        pass

    def mnar(self):
        """ Overwrites values with MNAR placed NaN's """
        pass

    def complete(self):
        """ Do nothing to the data """
        output = self.data
        return output