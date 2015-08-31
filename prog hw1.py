import urllib2
from HTMLParser import HTMLParser
import os


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        temp = ""
        temperature = ""
        #print attrs
        if(tag == "meta"):
            #print attrs[0]
            #print "\n"
            title = ('property','og:title')
            if(attrs[0] == title):
                print attrs[1]
                temp = attrs[1]
                for i in range(len(temp[1])):
                    if temp[1][i] == ".":
                        temperature = temperature + temp[1][i]
                    try:
                        x = int(temp[1][i])
                        if isinstance(x, int):
                            temperature = temperature + temp[1][i]
                    except:
                        continue
                print temperature
                        
                self.sendTemp(temperature)
    def handle_data(self, data):
        info = data
        #print "Encountered data: ", datas

    def sendTemp(self, temp):
        firstHalf = '<!DOCTYPE HTML PUBLIC "-//W3c//DTD HTML 4.01 Transitional//EN""http://www.w3.org/TR/html4/loose.dtd"><html lang="en"><head><meta http-equiv="content-type" content="text/html; charset=utf-8"><title>The Weather for Today</title></head><body><p>Todays Temperature in Burlington VT is: '
        secondHalf = " Degrees</p></body></html>"
        os.remove('todaysTemperature.html')
        f = open('todaysTemperature.html', 'w+')
        f.write(firstHalf)
        f.write(temp)
        f.write(secondHalf)
        f.close()



        
##class getTemp(self.temp):
##    for i in range(temp.length()):
##        print temp[i]


def Main():
    url = urllib2.urlopen(url = 'http://www.wunderground.com/weather-forecast/US/VT/Burlington.html')
    parser = MyHTMLParser()
    parser.feed(url.read())









Main()
