from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver import ActionChains
from time import sleep



@when('Product has image, name, price, description')
def verify_product(context):
    context.app.product.open_prod()
    context.app.product.verify_prod()


@when('User can zoom in product image, scroll thru images and close them (by clicking X)')
def prod_zoom_scroll(context):
    context.app.product.click_zoom_icn()
    context.app.product.verify_z_img()
    sleep(1)
    context.app.product.click_z_icon()
    sleep(1)
    context.app.product.click_z_right_arrow()
    sleep(1)
    context.app.product.click_z_right_arrow()
    context.app.product.click_z_right_arrow()
    sleep(1)
    context.app.product.click_z_left_arrow()
    context.app.product.click_z_left_arrow()
    context.app.product.click_z_close()


@when('Open the product')
def open_product(context):
    context.app.product.open_prod()


@when('User can add product to wishlist by hovering over product image and clicking on the heart icon')
def prod_wish_list(context):
    context.app.product.hover_prod_image()
    context.app.product.click_heart_icon()
    # context.app.latest_prod.check_wishlist()


@when('"Home" link takes user to Home Page {expected_url}')
def verify_home(context, expected_url):
    context.app.product.click_home_link()
    context.app.top_nav_menu.verify_page(expected_url)


@when('Category link takes users to correct category page')
def verify_category(context):
    context.app.product.click_cat_link()
    # context.app.results_page.verify_cat_result()