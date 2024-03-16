import json

class Transcript:

    def __init__(self, path):
        '''
        constructor method that opens the json file
        
        params:
            path: file path of json
        '''
        self.path = path
        self.f = open(path)
        self.data = json.load(self.f)

    def get_name(self):
        '''
        returns the name of the student
        '''
        return self.data["Student"]

    def __str__(self):
        '''
        returns a formatted transcript
        '''
        lineBreak = '|----------------------------|'
        s = '%s\n| %-26s |\n%s\n' % (lineBreak, self.get_name(), lineBreak)
        sems = []
        semClasses = []
        semesters = self.data["Semesters"]

        for i in semesters:
            sems.append(list(i.keys()))
            for j in i.values():
                course = list(j)
                semClasses.append(course)

        for i in range(len(sems)):
            s += '| %-26s |\n%s\n' % (sems[i][0], lineBreak)
            for j in range(len(semClasses[i])):
                s += '| %-26s |\n' % (semClasses[i][j])
            s += lineBreak + '\n'

        return(s)
        
        