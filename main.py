import requests
from bs4 import BeautifulSoup


# URL of the course page
url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=ASTR&course=200&section=101'

# act like a browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}

# download the page
source = requests.get(url, headers=headers).text
# parse the downloaded page
soup = BeautifulSoup(source, 'lxml')

# find the cell containing the number of available spots and store it in seats
table = soup.find_all('table')[3]
row = table.find_all_next('tr')[0]
seats = row.find_all_next('td')[1].strong.text
seats = int(seats)


