
def readFile():
    data = open('data.txt','r')
    readdata = data.read()
    data.close()
    return readdata

def printContent(meow):
    print(meow)

if(__name__ == '__main__'):
    print('hello world')
    fileResults = readFile()
    printContent(fileResults)


