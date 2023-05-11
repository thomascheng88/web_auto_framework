Feature: test_home_page

  Scenario: Visit homepage


    # Step 1
    Given guest open the browser
    When guest navigate to the homepage
    Then displays the homepage search
    And displays the homepage title

