import pytest
import pandas as pd
from src.transform.transform_dataframe import DataFrameTransformer

@pytest.fixture
def transformer():
    return DataFrameTransformer()

def test_format_data_dataframe_success(transformer):
    data = {'Data': ['Jan 01, 2020', 'Feb 02, 2021']}
    df = pd.DataFrame(data)
    
    result = transformer.format_data_dataframe(df, date_column='Data', date_format_in='%b %d, %Y')
    
    assert result['Data'][0] == '2020/01/01'
    assert result['Data'][1] == '2021/02/02'

def test_format_data_dataframe_failure(transformer):
    data = {'Data': ['Invalid date', 'Another invalid date']}
    df = pd.DataFrame(data)
    
    with pytest.raises(Exception, match='Error formatacao da coluna: '):
        transformer.format_data_dataframe(df)

def test_create_dataframe_success(transformer):
    data = [(1, 'A'), (2, 'B')]
    columns = ['Number', 'Letter']
    
    df = transformer.create_dataframe(data, columns)
    
    assert list(df.columns) == columns
    assert df.shape == (2, 2)

def test_create_dataframe_failure(transformer):
    data = [(1, 'A'), (2, 'B')]
    columns = 'Number'
    
    with pytest.raises(Exception, match="Error na criação do DataFrame"):
        transformer.create_dataframe(data, columns)
        
def test_select_n_rows_success(transformer):
    data = {'col1': range(20)}
    df = pd.DataFrame(data)
    
    result = transformer.select_n_rows(df, n=10)
    
    assert len(result) == 10
    assert result.iloc[0]['col1'] == 0
    assert result.iloc[9]['col1'] == 9

def test_select_n_rows_failure(transformer):
    df = 'This is not a DataFrame'
    
    with pytest.raises(Exception, match="Error na selecao das 10 linhas"):
        transformer.select_n_rows(df, n=10)