'''
Created on Jan 23, 2023

@author: Jim Lakis


'''

from dataclasses import dataclass
import pandas


@dataclass
class TimeSeriesRunningPercentChange:
    
    ''' Returns a Pandas dataframe of running percent differences bewteen a previous value and more recent value.
    Required parameter is a dataframe of dates and values formatted as in the example below.
    
    df.head(5)
    df.dtypes
    
        date    value
    0 2022-10-01  298.012
    1 2022-09-01  296.808
    2 2022-08-01  296.171
    3 2022-07-01  296.276
    4 2022-06-01  296.311
    date     datetime64[ns]
    value           float64
    dtype: object
    
    '''
    
    time_series : pandas.core.frame.DataFrame
    
    
    @property
    def return_running_average(self):
        ''' Return example...
        
        df.head(5)
        df.dtypes
        
                date     value
        0 2022-10-01  0.405649
        1 2022-09-01  0.215078
        2 2022-08-01 -0.035440
        3 2022-07-01 -0.011812
        4 2022-06-01  1.373608
        date     datetime64[ns]
        value           float64
        dtype: object
        
        '''
        
        temporary_series = self.time_series["value"]
        temporary_series.drop([0], inplace = True)
        temporary_series.reset_index(drop=True, inplace = True)
        self.time_series["previous_value"] = temporary_series
        self.time_series.rename(columns = {"value": "recent_value"}, inplace = True, errors="raise")
        self.time_series["percentage_change"] = ((self.time_series["recent_value"] - self.time_series["previous_value"]) / self.time_series["previous_value"] ) * 100
        self.time_series.drop(columns=['recent_value', 'previous_value'], inplace = True)
        self.time_series.rename(columns = {"percentage_change": "value"}, inplace = True, errors="raise")
        return self.time_series