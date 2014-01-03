Feature: As a guest of the wedding
	I want an RSVP form
	So that I can let the wedding know whether I'm attending

@wip
Scenario: Log in to the RSVP
	Given I am on the RSVP page
	When I enter my credentials
	I should be directed to the "http://localhost:8000/rsvp/yes/" page
