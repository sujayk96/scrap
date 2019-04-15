from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
#from mathematicians import simple_get

def simple_get(url):
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_resp(resp):
				return resp.content
			else:
				None
	except RequestException as e:
		log_error('Error returned to request {0} to {1}'.format(url, str(e)))
		return None

def is_good_resp(resp):
	resp_content = resp.headers['Content-Type'].lower()
	return(resp.status_code == 200
		and resp_content is not None
		and resp_content.find('html') > -1)

def log_error(e):
	print(e)

def get_names():
	url = 'https://www.inspiringleadershipnow.com/most-inspiring-leaders-redefine-leadership/'
	raw_html = simple_get(url)

	if raw_html is not None:
		html = BeautifulSoup(raw_html, 'html.parser')
		names = set()

		for h2 in html.select('h2'):
			#print(h2.text)
			if len(h2.text) > 0:
				names.add(h2.text)
		return list(names)

	raise Exception('Error retrieving contents at {}'.format(url))

names = get_names()
print(names.sort())