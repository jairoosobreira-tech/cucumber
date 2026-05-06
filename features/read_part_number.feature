Feature: Read ECU Part Number via UDS

  Scenario: Read valid part number DID
    Given the ECU is powered on
    And diagnostic session is "default"
    When I send a UDS request "0x22 F187"
    Then the response should be positive
    And the DID "F187" should return a valid part number

  Scenario: Read part number in extended session
    Given the ECU is powered on
    And diagnostic session is "extended"
    When I send a UDS request "0x22 F187"
    Then the response should be positive
    And the DID "F187" should return a valid part number

  Scenario: Read invalid DID
    Given the ECU is powered on
    When I send a UDS request "0x22 F999"
    Then the response should be negative