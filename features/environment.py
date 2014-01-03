from selenium import webdriver  
  
#def before_all(context):  
#    context.webdriver.get("http://google.com")

def after_all(context):  
    context.webdriver.quit()  