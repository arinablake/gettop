# Created by arina at 8/28/20
Feature: Browse Categories feature
  # Enter feature description here

  Scenario: Browse Categories scenarios
    Given Open https://gettop.us/ page
    When BROWSE OUR CATEGORIES text is shown (browse categories)
    When 4 correct categories are shown
    Then Upon clicking on each category, correct page opens