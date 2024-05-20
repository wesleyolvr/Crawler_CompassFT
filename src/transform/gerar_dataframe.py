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

    def format_data_dataframe(self, df, date_column='Data', date_format='%b %d, %Y'):
        try:
            self.logger.info(f'Formatando coluna data" {date_column}" com o formato ano/mes/dia".')
            df[date_column] = pd.to_datetime(df[date_column], format=date_format)
            df[date_column].dt.strftime('%Y/%m/%d')
            return df
        except Exception as e:
            self.logger.error(f'Error formatacao da coluna ano/mes/dia: {e}')
            raise Exception(f'Error formatacao da coluna ano/mes/dia: {e}')

    def create_dataframe(self, data, columns):
        try:
            self.logger.info(f'criacao do DataFrame com colunas: {columns}')
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