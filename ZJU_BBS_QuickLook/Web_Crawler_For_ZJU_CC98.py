#www.cc98.org/list.asp?boardid=248&page=1
#!/usr/bin/python
# -*- coding: latin-1 -*-
from bs4 import BeautifulSoup

import urllib2
page = urllib2.urlopen("http://www.cc98.org/list.asp?boardid=248&page=1")
whole_soup = BeautifulSoup(page)
soup_tbody = whole_soup.form.table.tbody
soup_tr_list = soup_tbody.find_all('tr')
soup_tr_list.pop(0)
soup_tr_list.pop(1)
soup_td_list = []
soup_td_list_temp = []
for soup_tr in soup_tr_list:
    soup_td_list_temp = soup_tr.find_all('td')
    soup_td_list.append(soup_td_list_temp[1])
soup_td_list.pop(0)
for soup_td in soup_td_list:
    print(soup_td.a.span.get_text())
