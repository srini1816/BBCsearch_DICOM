Feature: BBC Homepage Login

  Scenario: Login to BBC Home page with valid Credentials
    Given I launch Chrome Browser
    When I open BBC Home page
    And Enter username "srinivasreddy.tst@gmail.com" and password "Prahi@1816"
    And Click login button
    Then User must login to the Dashboard page

  Scenario Outline: Login to BBC Homepage with invalid credentials

    Given I launch chrome browser
    When I open BBC home page
    And Enter username "<username>" and password "<password>"
    And Click login button
    Then User should not login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | admin    | adminxyz |
