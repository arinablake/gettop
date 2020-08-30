# Created by arina at 8/28/20
Feature: GetTop logo

#  Scenario: GetTop logo takes to https://gettop.us/
#    Given Open https://gettop.us/ page
#    When GetTop logo is clickable
#    Then It takes to https://gettop.us/


  Scenario Outline: User can search for existing product and sees correct results
    Examples:
    |existing_product|
    |IPHONE  |
    |MACBOOK |
    |IPAD    |
    Given Open https://gettop.us/ page
    When User can search for <existing_product>
    Then User can see <existing_product> in results

  Scenario Outline: User can search for non-existing product and sees "No products were found matching your selection."
    Examples:
    |nonexisting_product|
    |SUSHI  |
    |PIZZA    |
    |VITAMINS   |
    Given Open https://gettop.us/ page
    When User can search for <nonexisting_product>
    Then User sees No products were found matching your selection
