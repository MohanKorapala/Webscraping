from twilio.rest import Client
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

sid = "Enter your account SID:"
auth = "Enter your authentication key:"

client - Client(sid,auth)

twilionumber = "Enter your Twilio Number:"
number = "Enter your number:"

url = "https://crypto.com/price/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url,headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,"html.parser")

rows = soup.findAll("tr")
for row in rows [1:6]:
    columns = row.findAll("td")

    rank = columns[1].text.strip()
    name = columns[2].find('span',attrs={'class':"chakra-text css-1mrk1dy"}).text.strip()
    symbol = columns[2].find('span',attrs={'class':'chakra-text css-ft1qn5'}).text.strip()
    price = float(columns[3].find('div',attrs={'class':"css-b1ilzc"}).text.strip().replace('$','').replace(',',''))
    percentageChange = columns[4].text.strip()

    alert = False
    if symbol == 'BTC':
        if price < 40000:
            alert = True
            pass
    elif symbol == 'ETH':
        if price <3000:
            alert = True
            pass

    print()
    print(f"Ranking: {ranking}")
    print(f"Currency: {name} ({symbol})")
    print(f"Current Price: ${price} ({percentageChange})")
    if alert:
        print("Sent text message, Buy!")
        textmessage = client.messages.create(to=myNumber, from_=twilioNumber, body=f"The price of {name} has dropped! You should buy now!")
    print()
    if ranking != '5':
        input("Press any key to continue ")