from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)
Config.set('kivy','window_icon','data/friday/res/icon.ico')
#from kivy.core.window import Window

from requests_oauthlib import OAuth1Session
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
SIGNIN_URL = 'https://api.twitter.com/oauth/authenticate'

consumer_key = None
consumer_secret = None

ret = None, None

class Root(Screen):
	def allow(self):
		Clock.schedule_once(self.login, 0.1)
	def login(self, dt):
		oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret, callback_uri='oob')

		resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)

		url = oauth_client.authorization_url(AUTHORIZATION_URL)

		driver = webdriver.Firefox()
		driver.get(url)
		WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.ID, "code-desc")))
		src = driver.page_source.split("\n")
		driver.close()
		pincode = ""
		for line in src:
			if '<kbd aria-labelledby="code-desc">' in line:
				pincode = re.findall(r"[\d]+", line)[0]
				break

		oauth_client = OAuth1Session(consumer_key, 
		                             client_secret=consumer_secret,
		                             resource_owner_key=resp.get('oauth_token'),
		                             resource_owner_secret=resp.get('oauth_token_secret'),
		                             verifier=pincode)
		try:
			resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
		except ValueError as e:
			raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)
		global ret
		ret = resp.get('oauth_token'), resp.get('oauth_token_secret')
		App.get_running_app().stop()

	def deny(self, *largs):
		exit()

class Permission(App):
	def build(self):
		self.icon = 'data/friday/res/icon.ico'
		return Root()

def get(para_consumer_key, para_consumer_secret):
	global consumer_key
	global consumer_secret
	consumer_key, consumer_secret = para_consumer_key, para_consumer_secret
	Permission().run()
	return ret