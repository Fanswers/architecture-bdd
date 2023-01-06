import requests
from bs4 import BeautifulSoup

# # Fetch the HTML content
# response = requests.get('https://www.info-concert.com/departement/')
# html_content = response.text
#
# # Parse the HTML content
# soup = BeautifulSoup(html_content, 'html.parser')
#
# # Find the elements containing concert information
# concerts = soup.find_all('div', class_='card')
#
# # Extract the desired information from each element and store it in a list
# concert_data = []
# for concert in concerts:
#     title = concert.find('h4').text
#     date = concert.find('span', class_='date').text
#     location = concert.find('span', class_='location').text
#     concert_info = {
#         'title': title,
#         'date': date,
#         'location': location
#     }
#     concert_data.append(concert_info)

