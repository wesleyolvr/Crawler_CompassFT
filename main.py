from src.transform.gerar_dataframe import DataFrameTransformer
from src.extract.crawler import CrawlerCompassFT

crawler = CrawlerCompassFT()
dados = crawler.run()


transformer = DataFrameTransformer()
colunas = ["Ticker", "Valor", "Data"]
df = transformer.create_dataframe(dados, colunas)
df = transformer.format_data_dataframe(df)
top_df = transformer.select_n_rows(df, 10)
print(top_df)