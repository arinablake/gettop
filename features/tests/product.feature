# Created by arina at 8/31/20
Feature: Product feature
  # Enter feature description here

  Scenario:  Product has image, name, price, description; zooming and scrolling; "Home" link takes user to Home Page
    Given Open https://gettop.us/ page
    When Product has image, name, price, description
    When User can zoom in product image, scroll thru images and close them (by clicking X)
    When "Home" link takes user to Home Page https://gettop.us/

#  not working - giving a stale element exception for some reason (but the page didn't refresh, so don't know why)
  Scenario:  User can add product to wishlist by hovering over product image and clicking on the heart icon
     Given Open https://gettop.us/ page
     When Open the product
     When User can add product to wishlist by hovering over product image and clicking on the heart icon

  Scenario:  Category link takes users to correct category page
    Given Open https://gettop.us/ page
    When Open the product
    When Category link takes users to correct category page


#  Product page - no social network logos/links on Chrome 85 !! bugs:
#Social network logos are present: FB, Twitter, Email, Pinterest LinkedIn
#Clicking on a social network link opens a new window to login to social network