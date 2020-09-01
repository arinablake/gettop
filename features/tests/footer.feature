# Created by arina at 8/31/20
Feature: Footer features
  # Enter feature description here

  Scenario:  Footer shows Best Selling, Latest, Top Rated categories
    Given Open https://gettop.us/ page
    When Footer shows Best Selling, Latest, Top Rated categories
#    When All products in the footer have price, name, star-rating
  #bug - no star rating in 1 prod - test fails

    When Copyright 2020 shown in footer
    When Footer has button to go back to top
    Then Footer has working links to all product categories