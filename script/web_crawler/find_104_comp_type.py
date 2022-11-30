import requests
from bs4 import BeautifulSoup

url='https://www.104.com.tw/company/search/'

session = requests.session()
query_params = {'jobsource': 'tab_job_to_cs'}
comp_list = ['歐漾國際企業股份有限公司']

for comp_name in comp_list:
  query_params['keyword'] = comp_name
  resp = session.get(url, params=query_params)
  parser = BeautifulSoup(resp.text, "html.parser")
  first_comp=parser.find('div', class_="company-lists__list")
  comp_type=first_comp.select('span', class_='info-tags__text')[1].text
  
  print("公司[%s]類型: %s\n" % (comp_name, comp_type))
