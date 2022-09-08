import re

class Helper:

    # return integer from string if number is > 0, otherwise -1
    def getInt(self, s):
        if not s:
            s = "0"
        try: 
            if int(s) >= 0:
                return int(s)
        except ValueError:
            return -1
        return -1

    # check string s with regex pattern pattern
    def checkRegex(self, pattern, s):
        compiled_pattern = re.compile(pattern)
        matched = compiled_pattern.match(s)
        return False if matched is None  else True

    #change url with new offset for paging
    def changeUrl(self, url, newOffset):
        urlQuery = url.split('?')

        if len( urlQuery ) > 1:
            urlSplit = urlQuery[1].split('&')
            exists = False
            for i in range(len(urlSplit)):
                if ("offset=" in urlSplit[i]):
                    urlSplit[i] = "offset=" + str(newOffset)
                    exists = True

            value = '&'.join(urlSplit)

            if not exists:
                value = value + "&offset=" + str(newOffset)
        else:
            value = "&offset=" + str(newOffset)

        value = urlQuery[0] + '?' + value
        
        return value
        


