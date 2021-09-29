import requests
import psycopg2
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

host = '127.0.0.1'
user = 'postgres'
password = 'Genius1701'
database = 'old_harry'


req = requests.get('https://ignio.com/r/export/utf/xml/daily/com.xml')
with open('horo.html', 'r', encoding='utf-8') as file:
    for i in ET.parse(file).getroot():
        print(i.tag, i.attrib)

# try:
#     connection = psycopg2.connect(
#         host='127.0.0.1',
#         user='postgres',
#         password='Genius1701',
#         database='old_harry'
#     )
#     connection.autocomit = True
#     with connection.cursor() as cursor:
#         cursor.execute(
#             'SELECT version();'
#         )
#         print('Server version',
#               cursor.fetchone())
#
# except Exception as ex:
#     print(ex)
# finally:
#     if connection:
#         connection.close()
#         print('CLOSE')

