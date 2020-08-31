from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Clicking on Cart icon opens {expected} Cart page if no products were added')
def click_logo(context, expected):
    context.app.top_nav_menu.click_cart_icon()
    context.app.results_page.verify_empty_cart(expected)

@when('Hovering over empty cart icon shows {expected} message')
def verify_hover_cart(context, expected):
    context.app.top_nav_menu.hover_cart_icon()
    context.app.top_nav_menu.check_empty_cart_widget()
    context.app.top_nav_menu.verify_cart_widget(expected)


@then('User can add product to cart, verify that price in top nav menu is correct')
def verify_cart_item_price(context):
    context.app.top_nav_menu.hover_cart_icon()
    context.app.top_nav_menu.check_cart_widget()
    context.app.top_nav_menu.verify_price_text()


@then('Verify that amount of items shown in top nav menu are correct')
def verify_cart_item_amount(context):
    # context.app.top_nav_menu.hover_cart_icon()
    # context.app.top_nav_menu.check_cart_widget()
    context.app.top_nav_menu.verify_item_amount_text()


@then('Verify correct products and subtotal shown')
def verify_prod_subtotal(context):
    context.app.top_nav_menu.verify_item_subtotal()


@then('Verify user can click on "View Cart" and is taken to {expected_url} cart page')
def verify_view_cart(context, expected_url):
    context.app.top_nav_menu.verify_cart_page(expected_url)
    # context.driver.back()
    # context.driver.back()


@then('Verify user can click on "Checkout" and is taken to {expected_url} checkout page')
def verify_checkout_cart(context, expected_url):
    context.app.top_nav_menu.hover_cart_icon()
    context.app.top_nav_menu.verify_checkout_page(expected_url)
    # context.driver.back()
    # context.driver.back()


@then('Verify user can remove a product')
def remove_prod(context):
    context.app.top_nav_menu.hover_cart_icon()
    context.app.top_nav_menu.remove_from_cart()


