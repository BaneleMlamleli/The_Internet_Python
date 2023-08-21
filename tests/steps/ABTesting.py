from behave import given, when, then
from pageobjects.ABTestingDomain import ABTestingDomain

@given('user is on the home page')
def home_page(context):
    context.current_page = ABTestingDomain()
    context.current_page.home_page

@when('user clicks on "{ab_testing}"')
def user_clicks_on_AB_Testing(context, ab_testing):
    context.current_page = context.current_page.click_link(ab_testing)

@then('user is redirected to the AB Test Control page')
def user_is_redirected_to_the_AB_Test_Control_page(context):
    context.current_page = context.current_page.redirect()