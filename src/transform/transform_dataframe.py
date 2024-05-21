import pandas as pd
import logging

class DataFrameTransformer:
    def __init__(self):
        self.logger = self._setup_logger()

    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('DataFrameTransformer')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    def format_data_dataframe(self, df, date_column='Data', date_format_in='%b %d, %Y',date_format_out='%Y/%m/%d'):
        try:
            self.logger.info(f'Transformando a coluna "{date_column}" para o formato {date_format_out}".')
            df[date_column] = pd.to_datetime(df[date_column], format=date_format_in)
            df[date_column] = df[date_column].dt.strftime(date_format_out)
            return df
        except Exception as e:
            self.logger.error(f'Error formatacao da coluna: {e}')
            raise Exception(f'Error formatacao da coluna: {e}')

    def create_dataframe(self, data, columns):
        try:
            self.logger.info(f'criando o DataFrame com as colunas: {columns}')
            df = pd.DataFrame(data, columns=columns)
            return df
        except Exception as e:
            self.logger.error(f'Error na criação do DataFrame: {e}')
            raise Exception(f'Error na criação do DataFrame: {e}')

    def select_n_rows(self, df, n=10):
        try:
            self.logger.info(f'Selecionando {n} linhas do DataFrame.')
            return df.head(n)
        except Exception as e:
            self.logger.error(f'Error na selecao das {n} linhas: {e}')
            raise Exception(f'Error na selecao das {n} linhas: {e}')