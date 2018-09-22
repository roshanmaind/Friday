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


def get(consumer_key, consumer_secret):
	from modules.twitter_interface import link_consent
	if not link_consent.consent():
		print("Exiting application on user request")
		return None, None
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

	oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret,
															 resource_owner_key=resp.get('oauth_token'),
															 resource_owner_secret=resp.get('oauth_token_secret'),
															 verifier=pincode)
	try:
			resp = oauth_client.fetch_access_token(ACCESS_TOKEN_URL)
	except ValueError as e:
			raise 'Invalid response from Twitter requesting temp token: {0}'.format(e)
	with open("text.txt", "w") as file:
		file.write(resp.get('oauth_token') + "\n" + resp.get('oauth_token_secret'))
	return resp.get('oauth_token'), resp.get('oauth_token_secret')
