# JapaneseFile

class open():
    def __init__(self, path, encoding='utf-8'):
        self.path = path
        #print('FilePath : ' + self.path)
        self.ReadFile = open(path, 'br')
        self.WriteFile = open(path, 'bw')
        self.encoding = encording
        print('Encoding : ' + self.encoding)
    def read():
        ReadBinary = fr.read()
        ReadText = read_a.decode(encoding)
        return ReadText
    def write(path, text):
        WriteTextBinary = text.encode(encoding)
        fw.write(WriteTextBinary)
