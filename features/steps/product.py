from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver import ActionChains



@when('Product has image, name, price, description')
def verify_product(context):
    context.app.product.verify_prod()

@when('User can zoom in product image, scroll thru images and close them (by clicking X)')
def prod_zoom_scroll(context):
    context.app.product.click_zoom_icn()
    # context.app.product.verify_z_img()
    # context.app.product.click_z_img()
    context.app.product.click_z_right_arrow()
    context.app.product.click_z_right_arrow()
    context.app.product.click_z_right_arrow()
    context.app.product.click_z_left_arrow()
    context.app.product.click_z_left_arrow()
    context.app.product.click_z_close()

@when('User can add product to wishlist by hovering over product image and clicking on the heart icon')
def prod_wishlist(context):
    context.app.product.hover_image()
    context.app.product.click_heart_icon()
    # context.app.latest_prod.check_wishlist()




