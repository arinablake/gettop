# Created by arina at 8/31/20
Feature: Adding to cart feature
  # Enter feature description here

  Scenario:  User can add product to cart
    Given Open https://gettop.us/ page
    When Open the product
    When User can add product to cart

  Scenario:  User can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    Given Open https://gettop.us/ page
    When Open the product
    When User can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart

  Scenario:  User can type in 10 amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    Given Open https://gettop.us/ page
    When Open the product
    When User can type in 10 amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    When User sees " ... have been added to your cart" confirmation upon adding items to cart

  Scenario:  User can type in 10 amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart
    Given Open https://gettop.us/ page
    When Open the product
    When User can click through multiple products by clicking back and forward arrows

  Scenario:  If product is out of stock, user sees 'Out of Stock', Add to Cart and Checkout buttons are not shown
    Given Open https://gettop.us/product/land-tee-jack-jones/ page
    Then If product is out of stock, user sees Out of Stock, Add to Cart and Checkout buttons are not shown
