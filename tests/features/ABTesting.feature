# @ABTesting
Feature: A/B Test Control

    Background: landing page with the initial link click
        Given user is on the home page
        When user clicks on "AB Testing"

    Scenario: A/B Test Control
        Then user is redirected to the AB Test Control page