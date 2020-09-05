from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('{expected} text is shown (latest products)')
def verify_section_title(context, expected):
    context.app.latest_prod.verify_title(expected)


TITLE = (By.CSS_SELECTOR, ' .section-title-main')
PRODUCT = (By.CSS_SELECTOR, '.flickity-viewport .product-small.col')
SALE_ICON = (By.CSS_SELECTOR, '.onsale')
IMAGE = (By.CSS_SELECTOR, '.box-image')
CATEGORY = (By.CSS_SELECTOR, '.category')
NAME = (By.CSS_SELECTOR, '.name')
PRICE = (By.CSS_SELECTOR, '.woocommerce-Price-amount.amount')
STAR_RATING = (By.CSS_SELECTOR, '.star-rating')


WISHLIST_ADDED = (By.CSS_SELECTOR, '#yith-wcwl-message')


@then('Every product has Sale icon, image, product category, name, price, and star-rating')
def verify_elements(context):
    prod_list = context.driver.find_elements(*PRODUCT)
    print(len(prod_list))

    for x in range(len(prod_list)):
        context.prod_on_sale = context.driver.find_elements(*PRODUCT)[x]
        si_prod_on_sale = context.prod_on_sale.find_elements(*SALE_ICON)
        assert len(si_prod_on_sale) > 0
        i_prod_on_sale = context.prod_on_sale.find_elements(*IMAGE)
        assert len(i_prod_on_sale) > 0
        c_prod_on_sale = context.prod_on_sale.find_elements(*CATEGORY)
        assert len(c_prod_on_sale) > 0
        n_prod_on_sale = context.prod_on_sale.find_elements(*NAME)
        assert len(n_prod_on_sale) > 0
        p_prod_on_sale = context.prod_on_sale.find_elements(*PRICE)
        assert len(p_prod_on_sale) > 0
        sr_prod_on_sale = context.prod_on_sale.find_elements(*STAR_RATING)
        assert len(sr_prod_on_sale) > 0


@when('User can click on heart icon to add to wishlist')
def click_heart(context):
    context.app.latest_prod.hover_image()
    context.app.latest_prod.click_heart_icon()
    context.app.latest_prod.check_wishlist()


@when('User can open product from Sale and add it to cart')
def open_add_product(context):
    context.app.latest_prod.click_image()
    context.app.product.click_add_t_c_btn()


@when('User can open product from Sale and see product price and description')
def open_see_product(context):
    context.app.latest_prod.click_image()
    context.app.product.verify_price()
    context.app.product.verify_description()


@when('User can open and close Quick View by clicking on closing X')
def quick_view_open_close(context):
    context.app.latest_prod.hover_image()
    context.app.latest_prod.click_quick_view()
    context.app.latest_prod.check_qv_window()
    context.app.latest_prod.close_qv()


@when('User can click Quick View and add product to cart')
def quick_view_add(context):
    context.app.latest_prod.hover_image()
    context.app.latest_prod.click_quick_view()
    context.app.latest_prod.check_qv_window()
    context.app.latest_prod.click_add_to_cart_btn()


@when('User can click Quick View and click through product images')
def quick_view_images(context):
    context.app.latest_prod.hover_image()
    context.app.latest_prod.click_quick_view()
    context.app.latest_prod.check_qv_window()
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_next_arrow()
    # sleep(1)
    context.app.latest_prod.click_prev_arrow()
    # sleep(1)
    context.app.latest_prod.click_prev_arrow()
    # sleep(1)
    context.app.latest_prod.click_prev_arrow()
    # sleep(1)