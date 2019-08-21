Feature: Search for an article

   As a user
   I want to be able to search for articles
   So that I can access the information that I am interested in

   Background:
     Given I am on the Qumu web site

   Scenario: Results found
     Given I enter the term Visa
     When I click search
     Then I should see results related to Visa

   Scenario: No results found
     Given I enter the term Bitcoin
     When I click search
     Then I should see that no results were found
     