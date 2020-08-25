# Created by arina at 8/25/20
Feature: Top banner feature
  # Enter feature description here

  Scenario: User can click right and left arrows to see top banners
    Given Open https://gettop.us/ page
    When Clicking left arrow
    Then User can see top banner 1
    When Clicking right arrow
    Then User can see top banner 2


  Scenario: User can click bottom dots to see top banners
    Given Open https://gettop.us/ page
    When Clicking bottom dots
    Then User can see top banner 1


  Scenario Outline: User can click on product banner and is taken to correct category page
    Examples:
      | search_word |
      | ipad        |
      | macbook     |
    Given Open https://gettop.us/ page
    When Clicking on product banner <search_word>
    Then User can see correct <search_word> page
