from src.transform.transform_dataframe import DataFrameTransformer
from src.extract.crawler import CrawlerCompassFT

def run_crawler():
    crawler = CrawlerCompassFT()
    return crawler.run()

def transform_data(data):
    transformer = DataFrameTransformer()
    colunas = ["Ticker", "Valor", "Data"]
    df = transformer.create_dataframe(data, colunas)
    df = transformer.format_data_dataframe(df)
    return transformer.select_n_rows(df, 10)

def main():
    dados = run_crawler()
    
    top_df = transform_data(dados)
    
    print(top_df)

if __name__ == "__main__":
    main()
