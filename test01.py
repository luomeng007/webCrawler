from urllib.request import urlopen
"""
python crawler for www.baidu.com
"""


class webCrawler:
    def mainProgram(self):
        url = "http://www.baidu.com"
        
        # send request
        response = urlopen(url)
        # read content
        info = response.read()
        
        # print state code
        print(response.getcode())
        # print real url
        print(response.geturl())
        # print response head
        print(response.info)


if __name__ == "__main__":
    main = webCrawler()
    main.mainProgram()