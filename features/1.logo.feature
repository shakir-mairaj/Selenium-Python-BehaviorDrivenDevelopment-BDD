Feature: Website Logo
  Scenario: Verify logo is present on homepage
    Given launch browser
    When open website homepage
    Then Verify logo is present
    And close browser