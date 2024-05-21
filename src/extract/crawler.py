import logging
from requests.exceptions import RequestException, Timeout, HTTPError, ConnectionError
from pyppeteer.errors import PyppeteerError
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from src.utils.utils import find_element, find_all_elements


class CrawlerCompassFT:

    def __init__(self):
        self.url = "https://www.compassft.com/indices/"
        self.session = HTMLSession()
        self.logger = self._setup_logger()
        self.responses_status_codes = {
            "200": "Request successful",
            "404": "Page not found",
            "500": "Internal server error",
            "503": "Service unavailable",
            "504": "Gateway timeout",
            "400": "Bad request",
            "403": "Forbidden",
            "429": "Too many requests",
        }

    @staticmethod
    def _setup_logger():
        logger = logging.getLogger('CrawlerCompassFT')
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
    def _get_status_message(self, status_code):
        return self.responses_status_codes.get(str(status_code), "Unknown status code")

    def _fetch_response(self):
        """Obtém a resposta do URL e trata os erros comuns de solicitação."""
        try:
            self.logger.info('Solicitando HTML.')
            response = self.session.get(self.url)
            response.raise_for_status()
            return response
        except ConnectionError:
            message = "Failed to connect to the server."
            self.logger.error(message)
            raise Exception(message)
        except Timeout:
            message = "The request timed out."
            self.logger.error(message)
            raise Exception(message)
        except HTTPError as http_err:
            status_code = http_err.response.status_code
            message = self._get_status_message(status_code)
            self.logger.error(message)
            raise Exception(message)
        except RequestException as req_err:
            message = f"An error occurred during the request: {req_err}"
            self.logger.error(message)
            raise Exception(message)

    def _render_html(self, response):
        """Renderiza o HTML da resposta e trata os erros de renderização."""
        try:
            self.logger.info('Renderizando HTML.')
            response.html.render()
        except PyppeteerError as render_err:
            message = f"An error occurred during rendering: {render_err}"
            self.logger.error(message)
            raise Exception(message)

    def _parse_html(self, response):
        try:
            self.logger.info('Parsendo HTML.')
            return BeautifulSoup(response.html.html, "html.parser")
        except Exception as e:
            message = f"Error parsing HTML: {e}"
            self.logger.error(message)
            raise Exception(message)

    def get_response(self):
        """Obtém e renderiza a pagina HTML, logando o resultado e gerando as exceções."""
        response = self._fetch_response()
        self._render_html(response)
        status_code = response.status_code
        message = self._get_status_message(status_code)

        if status_code != 200:
            self.logger.error(message)
            raise Exception(message)

        self.logger.info(message)

        return response

    def get_table_indice(self, response):
        soup_html = self._parse_html(response)
        table_indice = find_element(
            soup_element=soup_html,
            tag_name="table",
            attribute_name="id",
            attribute_value="table-indice",
        )

        if not table_indice:
            raise Exception("Table not found")

        self.logger.info("Tabela encontrada")
        return table_indice

    def get_rows_indices(self, table_indice):
        element_table_body = find_element(soup_element=table_indice, tag_name="tbody")
        rows_table_indice = find_all_elements(
            soup_element=element_table_body,
            tag_name="tr",
        )

        if not rows_table_indice:
            raise Exception("Indices not found")

        self.logger.info("Indices encontrados")

        return rows_table_indice

    def run(self):
        response = self.get_response()
        table_indice = self.get_table_indice(response)
        indices = self.get_rows_indices(table_indice)
        dados = []
        for indice in indices:
            Ticker = find_element(
                soup_element=indice,
                tag_name="td",
                attribute_name="data-label",
                attribute_value="Ticker",
            ).text
            Valor = find_element(
                soup_element=indice,
                tag_name="td",
                attribute_name="data-label",
                attribute_value="Last Value",
            ).text
            Data = find_element(
                soup_element=indice,
                tag_name="td",
                attribute_name="data-label",
                attribute_value="As of",
            ).text

            dados.append((Ticker, Valor, Data))

        if not dados:
            raise Exception("Dados not found")
        
        self.logger.info("Dados encontrados")
        return dados


if __name__ == "__main__":
    crawler = CrawlerCompassFT()
    dados = crawler.run()
    print(dados)