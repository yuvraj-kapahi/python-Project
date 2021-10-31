from flask import Flask,render_template,request
from selenium import webdriver
from getpass import getpass
app=Flask(__name__)
@app.route("/")
def la():
	return render_template('la.html')
@app.route("/chef")
def code():
	return render_template('chef.html')
@app.route("/loginc",methods=["POST"])
def opencode():
	a=request.form["username"]
	c=request.form["password"]
	browser=webdriver.Chrome('E:\pyflask\chromedriver.exe')
	browser.get("https://codechef.com")
	username = browser.find_element_by_id('edit-name')             
	password = browser.find_element_by_id('edit-pass')
	b=a
	username.send_keys(b)
	password.send_keys(c)
	login_button = browser.find_element_by_id("edit-submit")
	login_button.click()
	return "Succesfully login"
@app.route("/face")
def faceb():
	return render_template('face.html')
@app.route("/loginf",methods=["POST"])
def openface():
	a=request.form["username"]
	c=request.form["password"]
	browser=webdriver.Chrome('E:\pyflask\chromedriver.exe')
	browser.get("https://www.facebook.com")
	username=browser.find_element_by_id("email")
	password=browser.find_element_by_id('pass')
	b=a    
	username.send_keys(b)
	password.send_keys(c)
	login_button = browser.find_element_by_id("u_0_d_Am")                    
	login_button.click()
	return "Succesfully login"
@app.route("/snap")
def snap():
	return render_template('gram.html')
@app.route("/logini",methods=["POST"])
def openinsta():
	a=request.form["username"]
	c=request.form["password"]
	browser=webdriver.Chrome('E:\pyflask\chromedriver.exe')
	browser.get("https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome")
	username=browser.find_element_by_id("username")
	password=browser.find_element_by_id('password')
	b=a    
	username.send_keys(b)
	password.send_keys(c)
	login_button = browser.find_element_by_xpath("//*[@id='login_form']/div[4]/button")                    
	login_button.click()
	return "Succesfully login"
@app.route("/link")
def linked():
	return render_template('linked.html')
@app.route("/loginl",methods=["POST"])
def openlink():
	a=request.form["username"]
	c=request.form["password"]
	browser=webdriver.Chrome('E:\pyflask\chromedriver.exe')
	browser.get("https://www.linkedin.com")
	username=browser.find_element_by_id("session_key")
	password=browser.find_element_by_id('session_password')
	b=a    
	username.send_keys(b)
	password.send_keys(c)
	login_button = browser.find_element_by_xpath("/html/body/main/section[1]/div[2]/form/button")                    
	login_button.click()
	return "Succesfully login"
@app.route("/insta")
def insta():
	return render_template('insta.html')
@app.route("/logins",methods=["POST"])
def opengram():
	a=request.form["username"]
	c=request.form["password"]
	browser=webdriver.Chrome('E:\pyflask\chromedriver.exe')
	browser.get("https://www.instagram.com/accounts/login/?hl=en")
	username=browser.find_element_by_xpath("//input[@name=\"username\"]")
	password=browser.find_element_by_xpath("//input[@name=\"password\"]")
	b=a
	username.send_keys(b)
	password.send_keys(c)
	login_button=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
	login_button.click()
	return "Succesfully login"
if __name__ == '__main__':
	app.run()