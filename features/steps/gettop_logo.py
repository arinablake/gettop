from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('GetTop logo is clickable')
def click_logo(context):
    context.app.top_nav_menu.click_logo()


@then('It takes to {expected_url}')
def verify_url(context, expected_url):
    context.app.top_nav_menu.verify_page(expected_url)


@when('User can search for {product}')
def search_prod(context, product):
    context.app.top_nav_menu.hover_icon()
    context.app.top_nav_menu.check_search_field()
    context.app.top_nav_menu.search_word(product)


@then('User can see {existing_product} in results')
def search_correct(context, existing_product):
    context.app.results_page.verify_result(existing_product)


# @when('User can search for {nonexisting_product}')
# def search_prod(context, nonexisting_product):
#     context.app.top_nav_menu.hover_icon()
#     context.app.top_nav_menu.check_search_field()
#     context.app.top_nav_menu.search_word(nonexisting_product)

@then('User sees {expected_text}')
def search_correct(context, expected_text):
    context.app.results_page.verify_ne_prod(expected_text)

# @when('User can search for {nonexisting_product}')
# def search_prod(context, nonexisting_product):
#     context.app.top_nav_menu.hover_icon()
#     context.app.top_nav_menu.check_search_field()
#     context.app.top_nav_menu.search_word(nonexisting_product)


@when('Clicking on Account icon opens Login form')
def verify_login_form(context):
    context.app.top_nav_menu.click_user_icon()
    context.app.top_nav_menu.check_login_form()

