from requests_html import HTMLSession

session = HTMLSession()

url = 'https://umtc.catalog.prod.coursedog.com/courses?cq=&page=1'

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

buttons = r.html.find('h6:first-child')

button_text = []
for button in buttons:
    button_text.append(button.text)

for button in button_text:
    print(button)