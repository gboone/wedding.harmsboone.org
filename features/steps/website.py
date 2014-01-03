from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Chrome(service_args=["--verbose"])

# get to the RSVP page
def getRSVP(self):
	driver.get("http://localhost:8000/rsvp")

# get element
def getElementbyID(id):
	driver.find_element(by=By.ID, value=id)

# send keys
def sendkeys(text):
	driver.sendkeys(text)

# hit submit
def submit(element):
	element.submit()

@given('I am on the RSVP page')
def step(context):
	context.getRSVP()

@when('I enter my credentials')
def step(context):
	getElementbyID()