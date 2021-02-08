Feature: To verify search functionality

  Scenario: Valid search
    Given a user on the main page
    When the user enters valid information in the search bar
    Then the list of available data displayed is filtered by that information

  Scenario: Valid search - No results found
    Given a user on the main page
    When the user enters valid information in the search bar
    And the information yields no results
    Then some information is displayed to inform the search yielded no results

  Scenario: Clear search
    Given a user on the main page
    And the information displayed is filtered by the search details
    When the user clear the search
    Then the full list of available data is displayed