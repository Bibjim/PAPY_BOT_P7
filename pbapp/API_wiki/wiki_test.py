# -*- coding: utf-8 -*-

from pbapp.API_wiki.wiki import Wiki


def test_id_article_online():
    apiwiki = Wiki()
    response_id = apiwiki.get_page_id_wiki(48.85837009999999, 2.2944813)
    assert response_id == 1359783


def test_content_article_online():
    apiwiki = Wiki()
    response_content = apiwiki.get_article_wiki(1359783)
    assert response_content[:14] == 'La tour Eiffel'


def test_apiwiki_get_page_id_offline(monkeypatch):
    """WikiPedia API test offline id page"""
    result = {
        'query': {
            'geosearch':
            [
                {
                    'pageid': 12
                }
            ]
        }
    }

    class MockRequests:
        """Mock class Requests"""

        def get(self, url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class Response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('pbapp.API_wiki.wiki.requests', MockRequests())

    apiwiki = Wiki()
    pageid = apiwiki.get_page_id_wiki(48.85837009999999, 2.2944813)

    assert pageid == 12


def test_apiwiki_get_extract_offline(monkeypatch):
    """WikiPedia API test offline extract"""

    result = {
        'query': {
            'pages': {
                '12': {
                    'canonicalurl':
                    'https://fr.wikipedia.org/wiki/Tour_Eiffel',
                    'extract':
                    'La tour du Mordor'
                }
            }
        }
    }

    class MockRequests:
        """Mock class Requests"""

        def get(self, url, params):
            """Mock method get function"""

            return MockResponse(200)

    class MockResponse:
        """Mock class Response"""

        def __init__(self, code):
            """Wiki API code initialization"""

            self.status_code = code

        def json(self):
            """Mock method json function"""

            return result

    monkeypatch.setattr('pbapp.API_wiki.wiki.requests', MockRequests())
    apiwiki = Wiki()
    extract_text = apiwiki.get_article_wiki(12)
    assert extract_text == 'La tour du Mordor'