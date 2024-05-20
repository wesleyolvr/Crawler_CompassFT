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

    def select_top_n_rows(self, df, n=10):

        try:
            self.logger.info(f'Selecionando {n} linhas do DataFrame.')
            return df.head(n)
        except Exception as e:
            self.logger.error(f'Error na selecao das {n} linhas: {e}')
            raise Exception(f'Error na selecao das {n} linhas: {e}')

    def filter_by_column_value(self, df, column, value):

        try:
            self.logger.info(f'Filtering DataFrame where column "{column}" is equal to "{value}".')
            filtered_df = df[df[column] == value]
            return filtered_df
        except Exception as e:
            self.logger.error(f'Error filtering DataFrame by column "{column}" and value "{value}": {e}')
            raise Exception(f'Error filtering DataFrame by column "{column}" and value "{value}": {e}')

    def add_column(self, df, column_name, default_value=None):

        try:
            self.logger.info(f'Adding column "{column_name}" with default value "{default_value}".')
            df[column_name] = default_value
            return df
        except Exception as e:
            self.logger.error(f'Error adding column "{column_name}": {e}')
            raise Exception(f'Error adding column "{column_name}": {e}')



if __name__ == "__main__":
    # Exemplo de uso da classe DataFrameTransformer
    transformer = DataFrameTransformer()

    # Criar um DataFrame
    data = [
        ['May 17, 2024', 100, 200],
        ['May 18, 2024', 150, 250],
        ['May 19, 2024', 200, 300]
    ]
    columns = ['Data', 'Value1', 'Value2']
    df = transformer.create_dataframe(data, columns)

    # Formatar a coluna de data
    df = transformer.format_data_dataframe(df)

    # Selecionar as top 10 linhas (neste caso, todas, pois só temos 3 linhas)
    top_df = transformer.select_top_n_rows(df, 10)

    # Filtrar o DataFrame por um valor específico
    filtered_df = transformer.filter_by_column_value(df, 'Value1', 150)

    # Adicionar uma nova coluna
    df_with_new_column = transformer.add_column(df, 'NewColumn', 'DefaultValue')

    print(df)
    print(top_df)
    print(filtered_df)
    print(df_with_new_column)
