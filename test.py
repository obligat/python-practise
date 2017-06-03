def loadMPG():
    medianAndDeviation = []
    f = open('/home/dujinqiao/Documents/python-practise/mpgTrainingSet.txt')
    lines = f.readlines()
    print lines
    f.close()
    format = lines[0].strip().split('\t')
    data = []
    for line in lines[1:]:
        fields = line.strip().split('\t')
        ignore = []
        vector = []
        for i in range(len(fields)):
            if format[i] == 'num':
                vector.append(float(fields[i]))
            elif format[i] == 'comment':
                ignore.append(fields[i])
            elif format[i] == 'class':
                classification = fields[i]
        data.append((classification, vector, ignore))
    print data


loadMPG()
