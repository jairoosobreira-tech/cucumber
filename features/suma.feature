Feature: Suma simple

  Scenario: Sumar dos numeros
    Given I have two numbers
    When I add them
    Then the result should be 5