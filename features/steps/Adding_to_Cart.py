from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('User can add product to cart')
def adding_to_cart(context):
    context.app.product.click_prod_add_tc()


@when('User can click - and + to modify amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart')
def cart_plus_minus(context):
    context.app.product.click_cart_plus()
    context.app.product.click_cart_plus()
    context.app.product.click_cart_plus()
    context.app.product.click_cart_minus()
    context.app.product.get_qty_input()
    context.app.product.click_prod_add_tc()
    context.app.product.verify_cart_item_amount_text()

@when('User can type in {num} amount of items to add to cart, upon adding to cart, correct amount of items shown in the cart')
def cart_type_num(context, num):
    context.app.product.qty_input(num)
    context.app.product.click_prod_add_tc()
    context.app.product.verify_cart_item_amount_text()

@when('User sees " ... have been added to your cart" confirmation upon adding items to cart')
def add_tc_confirm(context):
    context.app.product.verify_add_to_cart_confirm()


@when('User can click through multiple products by clicking back and forward arrows')
def prod_arrows(context):
    context.app.product.click_prod_left_arrow()
    context.app.product.click_prod_left_arrow()
    context.app.product.click_prod_right_arrow()


@given('Open https://gettop.us/product/land-tee-jack-jones/ page')
def open_oos_prod(context):
    context.driver.get('https://gettop.us/product/land-tee-jack-jones/')


@then('If product is out of stock, user sees {expected}, Add to Cart and Checkout buttons are not shown')
def out_of_stock(context, expected):
    context.app.product.verify_out_of_stock(expected)
    context.app.product.verify_out_of_stock_btns()
