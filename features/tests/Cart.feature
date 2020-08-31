# Created by arina at 8/31/20
Feature: Cart Icon features
  # Enter feature description here

  Scenario: Clicking on Cart icon opens Empty Cart page if no products were added
    Given Open https://gettop.us/ page
    When Clicking on Cart icon opens Empty Cart page if no products were added

  Scenario: Hovering over empty cart icon shows "No products in the cart." message
    Given Open https://gettop.us/ page
    When Hovering over empty cart icon shows No products in the cart message

  Scenario: User can add product to cart, verify that price in top nav menu is correct
    Given Open https://gettop.us/ page
    When User can click Quick View and add product to cart
    Then User can add product to cart, verify that price in top nav menu is correct
    Then Verify that amount of items shown in top nav menu are correct
    Then Verify correct products and subtotal shown
    Then Verify user can click on "View Cart" and is taken to https://gettop.us/cart/ cart page

  Scenario: User can add product to cart, verify that price in top nav menu is correct
    Given Open https://gettop.us/ page
    When User can click Quick View and add product to cart
    Then Verify user can click on "Checkout" and is taken to https://gettop.us/checkout/ checkout page

  Scenario: User can add product to cart, verify that price in top nav menu is correct
    Given Open https://gettop.us/ page
    When User can click Quick View and add product to cart
    Then Verify user can remove a product

