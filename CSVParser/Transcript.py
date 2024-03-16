'''
This is a transcript. I hope that the code is not too hard to read; tried my best
'''

class Transcript:

    def __init__(self, tscript, stuName):
        self.stuName = stuName
        self.tscript = tscript

    def CSVtoList(self):
        '''
        converts the CSV to a list
        
        returns: list
        '''
        listTScript = []
        for line in self.tscript:
            line = line.strip().split(',')
            listTScript.append(line)
        return listTScript

    def computeGPA(self, tscript):
        '''
        iterates over each course, stores the grade in a list, calculates the gpa. 
        This function is a little janky. I'm going to try to optimize it better. I believe
        this function will only work properly once the CSV has been converted to a list
        
        parameters: transcript
        
        returns: float
        '''
        #dictionary to store grade point values
        gradePoint = {
            'A' : 4.0,
            'B' : 3.0,
            'C' : 2.0,
            'D' : 1.0,
            'F' : 0.0,
        }

        grades = []
        #iterates over each grade and appends them to list 'grades'; matches the grade to the
        #value in the dict
        for course in tscript:
            grade = course[3]
            if grade in gradePoint:
                grades.append(gradePoint[grade])
        gpa = sum(grades) / len(grades)
        return gpa

    def __str__(self):
        '''
        returns a formatted transcript
        returns: str
        '''
        lineBreak = '|-----------------------------------|'
        string = ''
        #prints student name
        string += '%s\n| %-33s |\n' % (lineBreak, self.stuName)
        string += f'{lineBreak}\n'
        #converts the CSV to a list so it can be indexed
        tscript = self.CSVtoList()
        gpa = self.computeGPA(tscript)
        #prints header: 'Year Semester Course Grade'
        string += ('| %-4s | %-8s | %-7s | %-5s |\n%s\n' % (
                    tscript[0][0], tscript[0][1], tscript[0][2], tscript[0][3], lineBreak))

        #iterates over each class
        for line in range(1, len(tscript)):
            course = tscript[line]
            string += ('| %-4s | %-8s | %-7s | %-5s |\n' % (
                course[0], course[1], course[2], course[3]))
            semester = course[1]
            #Checks if the next class is in a different semester. If it is, it will insert a line break
            try:
                if semester != tscript[line +1][1]:
                    string += f'{lineBreak}\n'
            #IndexError raised if tscript[line + 1] is out of bounds. Probably a better workaround for this, just had trouble finding it
            except IndexError:
                string += lineBreak

        #prints the overall gpa
        string += ('\n| Overall GPA: %-20.2f |\n%s' % (gpa, lineBreak))  
        return string