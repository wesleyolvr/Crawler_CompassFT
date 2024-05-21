import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException
from pyppeteer.errors import PyppeteerError
from src.extract.crawler import CrawlerCompassFT

@pytest.fixture
def crawler():
    return CrawlerCompassFT()

@patch('src.extract.crawler.HTMLSession.get')
def test_fetch_response_success(mock_get, crawler):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    response = crawler._fetch_response()
    assert response.status_code == 200

@patch('src.extract.crawler.HTMLSession.get')
def test_fetch_response_connection_error(mock_get, crawler):
    mock_get.side_effect = ConnectionError
    with pytest.raises(Exception, match="Failed to connect to the server."):
        crawler._fetch_response()

@patch('src.extract.crawler.HTMLSession.get')
def test_fetch_response_timeout(mock_get, crawler):
    mock_get.side_effect = Timeout
    with pytest.raises(Exception, match="The request timed out."):
        crawler._fetch_response()


@patch('src.extract.crawler.HTMLSession.get')
def test_fetch_response_http_error(mock_get, crawler):
    mock_response = MagicMock()
    mock_get.return_value = mock_response
    mock_response.raise_for_status.side_effect = HTTPError(response=MagicMock(status_code=404))

    with pytest.raises(Exception, match="Page not found"):
        crawler._fetch_response()

@patch('src.extract.crawler.HTMLSession.get')
def test_fetch_response_request_exception(mock_get, crawler):
    mock_get.side_effect = RequestException("Some request error")
    with pytest.raises(Exception, match="An error occurred during the request: Some request error"):
        crawler._fetch_response()
        
@patch('src.extract.crawler.HTMLSession')
def test_render_html_pyppeteer_error(mock_HTMLSession, crawler):
    mock_html_session = MagicMock()
    mock_HTMLSession.return_value = mock_html_session
    mock_response = MagicMock()
    mock_html_session.get.return_value = mock_response
    mock_response.html.render.side_effect = PyppeteerError("Some Pyppeteer error")
    
    with pytest.raises(Exception, match="An error occurred during rendering: Some Pyppeteer error"):
        crawler._render_html(mock_response)

@patch('src.extract.crawler.BeautifulSoup')
def test_parse_html_bs4_error(mock_BeautifulSoup, crawler):
    mock_soup = MagicMock()
    mock_soup.html.html = '<html></html>'
    mock_BeautifulSoup.side_effect = Exception("Some BeautifulSoup error")
    
    with pytest.raises(Exception, match="Error parsing HTML: Some BeautifulSoup error"):
        crawler._parse_html(mock_soup)
        

@patch('src.extract.crawler.HTMLSession.get')
def test_get_response_success(mock_get, crawler):
    mock_response = MagicMock()
    mock_get.return_value = mock_response
    mock_response.status_code = 200
    
    response = crawler.get_response()
    assert response.status_code == 200