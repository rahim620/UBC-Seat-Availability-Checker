# UBC Course Seat Availability Checker

### Sends email if a seat becomes available in a specified ubc course

Uses the requests library to download the source code and parses it with BeautifulSoup
to find the number of total seats available.

Sends an email notification if availability is greater than 0 using smtplib and EmailMessage 
libraries.