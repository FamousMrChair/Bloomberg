import blpapi
import pdblp
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time, os
con = pdblp.BCon(debug=False, port=8194, timeout=5000)
con.start()
df3 = con.bdib('SPY Equity', '2015-06-19T09:30:00', '2015-06-19T15:30:00', eventType='TRADE', interval=15)
df3.head()
"""
def sendIntradayTickRequest(session, options):
refDataService = session.getService("//blp/refdata")
request = refDataService.createRequest("IntradayTickRequest")

# only one security/eventType per request
request.set("security", options.security)

# Add fields to request
eventTypes = request.getElement("eventTypes")
for event in options.events:
    eventTypes.appendValue(event)

# All times are in GMT
if not options.startDateTime or not options.endDateTime:
    tradedOn = getPreviousTradingDate()
    if tradedOn:
        startTime = datetime.datetime.combine(tradedOn,
                                              datetime.time(15, 30))
        request.set("startDateTime", startTime)
        endTime = datetime.datetime.combine(tradedOn,
                                            datetime.time(15, 35))
        request.set("endDateTime", endTime)
else:
    if options.startDateTime and options.endDateTime:
        request.set("startDateTime", options.startDateTime)
        request.set("endDateTime", options.endDateTime)

if options.conditionCodes:
    request.set("includeConditionCodes", True)

print "Sending Request:", request
session.sendRequest(request)
"""

pdblp.bdp('NVDA US Equity', ['Security_Name', 'GICS_Sector_Name'])
"""
# print some data
print(con.bdh('SPY US Equity', ['PX_LAST', 'VOLUME'],'20150629', '20150630'))
"""
"""
blacklist = ''
def makeHTMLTable(nums):
    s = '<table> \n'
    for x in nums:
        s = s + '  <tr> \n'
        for x in x:
            s = s + '    <td>' + str(x) + '</td>\n'
        s = s + '  </tr> \n'
    s = s + '</table>'
    return s
import requests
import re
url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X,"}

headers = {
    'x-api-key': "flBW4StnnO7UJtOgznNor7yWlObKJag45q9KyDug"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
trending = response.text
delimiters = 'regularMarketPreviousClose', 'regularMarketDayLow','regularMarketDayHigh', 'regularMarketPrice', 'symbol'
def split(delimiters, string, maxsplit=0):
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)
trending = split(delimiters,trending)
trendingstocks = ''
for i in trending:
    while "{" in i:
        i = i.replace("{",'')
    while "}" in i:
        i = i.replace("}",'')
    while ":" in i:
        i = i.replace(":",'')
    while "," in i:
        i = i.replace(",",'')
    if ord(i[1]) >= 48 and ord(i[1]) <= 57:
        n = i.split('"')[1]
    else:
        n = i.split('"')[2] + ' '
    trendingstocks = trendingstocks + n + ' '
datav1 = trendingstocks.split('  ')
counter = 0
for i in datav1:
    datav1[counter] = i.split(' ')
    counter += 1
datav2 = datav1[1:-1]
stockstosend = ''
measure = False
time1 = 1000000000000000000000000
while measure == False:
    for i in datav2:
        if (float(i[1]) - float(i[0])) / float(i[1]) > 0.2 and i[4] not in blacklist:
            stockstosend = stockstosend + i[4]
            time1 = time.time()
        elif (float(i[0]) - float(i[2])) / float(i[2]) > 0.2 and i[4] not in blacklist: 
            stockstosend = stockstosend + i[4]
            time1 = time.time()
        elif abs(float(i[0])-float(i[3])) / float(i[3]) > 0.2 and i[4] not in blacklist:
            stockstosend = stockstosend + i[4]
            time1 = time.time()
        else:
            measure = True
        if time.time() > (time1 + 10) :
            measure = True
blacklist = blacklist + stockstosend
"""
