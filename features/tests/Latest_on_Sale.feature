# Created by arina at 8/26/20
Feature: Latest products on sale feature

  Scenario: LATEST PRODUCTS ON SALE text is shown, Every product has Sale icon, image, product category, name, price, and star-rating
    Given Open https://gettop.us/ page
    When LATEST PRODUCTS ON SALE text is shown (latest products)
    Then Every product has Sale icon, image, product category, name, price, and star-rating

  Scenario: User can click on heart icon to add to wishlist
    Given Open https://gettop.us/ page
    When User can click on heart icon to add to wishlist

  Scenario: User can open product from Sale and add it to cart
    Given Open https://gettop.us/ page
    When User can open product from Sale and add it to cart

  Scenario: User can open product from Sale and see product price and description
    Given Open https://gettop.us/ page
    When User can open product from Sale and see product price and description

  Scenario: User can open and close Quick View by clicking on closing X
    Given Open https://gettop.us/ page
    When User can open and close Quick View by clicking on closing X

  Scenario: User can click Quick View and add product to cart
    Given Open https://gettop.us/ page
    When User can click Quick View and add product to cart

  Scenario: User can click Quick View and click through product images
    Given Open https://gettop.us/ page
    When User can click Quick View and click through product images


