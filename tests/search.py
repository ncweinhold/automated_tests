# coding=utf-8
"""Search for an article feature tests."""
from functools import partial
from pytest_bdd import (
    given,
    parsers,
    scenario,
    then,
    when,
)

from pages.home_page import HomePage
from pages.search_overlay import SearchOverlay
from pages.search_results import SearchResultsPage

scenario = partial(scenario, '../features/search.feature')

@scenario('No results found')
def test_no_results_found():
    """No results found."""


@scenario('Results found')
def test_results_found():
    """Results found."""


@given('I am on the Qumu web site')
def i_am_on_the_qumu_web_site(driver, env):
    """I am on the Qumu web site."""
    driver.get(env['site'])


@given(parsers.parse(r'I enter the term {search_term}'))
def i_enter_the_term(driver, env, search_term):
    """I enter the provided search term."""
    home_page = HomePage(driver=driver, env=env)
    home_page.wait_for_load()
    home_page.click_search_icon()
    search_overlay = SearchOverlay(driver=driver, env=env)
    search_overlay.wait_for_load()
    search_overlay.enter_search_query(search_term)


@when('I click search')
def i_click_search(driver, env):
    """I click search."""
    search_overlay = SearchOverlay(driver=driver, env=env)
    search_overlay.submit_search_query()


@then('I should see results related to Visa')
def i_should_see_results_related_to_visa(driver, env):
    """I should see results related to 'Visa'."""
    results_page = SearchResultsPage(driver=driver, env=env)
    results_page.wait_for_load()
    assert results_page.results_were_found()


@then('I should see that no results were found')
def i_should_see_that_no_results_were_found(driver, env):
    """I should see that no results were found."""
    results_page = SearchResultsPage(driver=driver, env=env)
    results_page.wait_for_load()
    assert results_page.no_results_were_found()
    assert results_page.get_no_results_message() == \
        results_page.get_expected_no_results_message()