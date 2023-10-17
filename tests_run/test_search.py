import pytest

from DOMs.search_results import SearchResult

@pytest.mark.skip
def test_search(page):
    searchTest = SearchResult(page)
    #Szukany tekst
    searchTest.searchtest("camera")