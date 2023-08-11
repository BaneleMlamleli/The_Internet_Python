from behave import given, when, then
from hamcrest import assert_that, equal_to
from blender  import Blender
from pageobjects.ABTesting_Domain import ABTestingDomain

@given('user is on the welcome home page')
def home_page(context):
    context.ABTesting_Domain = ABTestingDomain
    context.ABTesting_Domain.welcome_page

@when('user clicks on "{link}"')
def user_clicks_on_AB_Testing(context, link):
    context.ABTesting_Domain = ABTestingDomain(link)
    context.ABTesting_Domain.click_link

@then('user is redirected to the "{ab_test_control}" page')
def user_is_redirected_to_the_AB_Test_Control_page(context, ab_test_control):
    context.ABTesting_Domain = ABTestingDomain(ab_test_control)
    context.ABTesting_Domain.redirect