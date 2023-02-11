"""
DataFrame Cleaning
==================

The script that defines the class the deals with cleaning the dataframe.

"""

import pandas as pd
from pathlib import Path


class DataSource:

    def __init__(self, df_source, sheets=None):

        # Detect what df_source is
        if isinstance(df_source, pd.DataFrame):
            self.df = df_source.copy(deep=True)

        # df_source is a string to a file
        elif isinstance(df_source, str):

            data_path = Path(df_source)

            # Is the path to a folder or file?
            if data_path.is_file():

                # Handle different file types and load them into pandas df
                if df_source.lower().endswith(".csv"):
                    pass

                elif df_source.lower().endswith(".xlsx"):
                    pass

                elif df_source.lower().endswith(".ods"):
                    pass

            elif data_path.is_dir():

                # TODO: Detect the files in the folder

                # TODO: Load and concatenate them

                # TODO: Handle headers
                pass

            # The data_path is not valid
            else:
                raise FileNotFoundError(f"The path "
                                        f"\"{data_path}\" is not valid.")

        # The type is not supported
        else:
            raise TypeError(f"\"{type(df_source)}\" is not supported.")

    def clean_names(self):
        pass

    def del_columns(self):
        pass

    def keep_columns(self):
        pass

    def del_row_with_null(self):
        pass

    def del_empty(self):
        pass

    def del_col_with_null(self):
        pass

    def format_as_datetime(self):
        pass
